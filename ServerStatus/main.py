# coding: utf-8
# course - msg.py
# 2019/9/15 12:49


import logging
import time
from platform import uname
from passlib.hash import pbkdf2_sha256
import os
from tornado import web, ioloop, httpserver, options
import json
import pymongo

root_path = os.path.dirname(__file__)
static_path = os.path.join(root_path, 'static')


class BaseHandler(web.RequestHandler):
    def data_received(self, chunk):
        pass


def mongo_db():
    client = pymongo.MongoClient()
    return client


class GameHandler(BaseHandler):

    def get(self):
        config_path = os.path.join(static_path, 'config', 'game.json')
        f = open(config_path)
        config = json.load(f)
        f.close()

        client = mongo_db()
        db = client['serverstatus']
        col = db['game_status']
        data = list(col.find())
        for item in data:
            item.pop('_id')

        results = {
            "column": config['column'],
            "data": data
        }
        self.write(results)


class IndexHandler(BaseHandler):
    def get(self):
        self.redirect('/static/pages/index.html')


class SSHandler(BaseHandler):
    def get(self):
        if self.get_secure_cookie('login'):

            config_path = os.path.join(static_path, 'config', 'ss.json')
            f = open(config_path)
            config = json.load(f)
            f.close()

            client = mongo_db()
            db = client['serverstatus']
            col = db['ss_status']
            data = list(col.find())
            for item in data:
                item.pop('_id')

            results = {
                "column": config['column'],
                "data": data
            }
            self.write(results)
        else:
            self.set_status(403)


class LoginHandler(BaseHandler):
    def post(self):
        password = self.get_body_argument('password')
        client = mongo_db()
        db = client['serverstatus']
        col = db['ss_auth']
        db_password = col.find_one()['password']

        result = pbkdf2_sha256.verify(password, db_password)
        if result:
            self.set_secure_cookie('login', 'abc')
        else:
            self.set_status(400)
            self.write({"message": "密码错误"})


class RunServer:
    handlers = [
        (r'/api/game', GameHandler),
        (r'/api/ss', SSHandler),
        (r'/api/login', LoginHandler),
        (r'/', IndexHandler),
        (r'/static/(.*)', web.StaticFileHandler, {'path': static_path}),
    ]
    settings = {
        "cookie_secret": "5Li05DtnQewDZq1mDVB3HAAhFqUu2vD2USnqezkeu+M=",
        "xsrf_cookies": False,
        "autoreload": True,
        'template_path': '.',
    }

    application = web.Application(handlers, **settings)

    @staticmethod
    def run_server(port=10000, host='127.0.0.1', **kwargs):
        tornado_server = httpserver.HTTPServer(RunServer.application, **kwargs, xheaders=True)
        tornado_server.bind(port, host)

        if uname()[0] == 'Windows':
            tornado_server.start()
        else:
            tornado_server.start(1)

        try:
            print('Server is running on http://{host}:{port}'.format(host=host, port=port))
            ioloop.IOLoop.instance().current().start()
        except KeyboardInterrupt:
            ioloop.IOLoop.instance().stop()
            print('"Ctrl+C" received, exiting.\n')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    options.define("p", default=10000, help="running port", type=int)
    options.define("h", default='127.0.0.1', help="listen address", type=str)
    options.parse_command_line()
    p = options.options.p
    h = options.options.h
    RunServer.run_server(port=p, host=h)
