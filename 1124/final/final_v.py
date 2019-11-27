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


class BaseHandler(web.RequestHandler):
    def data_received(self, chunk):
        pass


def mongo_db():
    client = pymongo.MongoClient()
    return client


class MessageHandler(BaseHandler):

    def get(self):
        if not self.get_secure_cookie('user'):
            self.redirect('/static/login.html')
        else:
            client = mongo_db()
            db = client['message']
            col = db['message']
            data = list(col.find())
            for item in data:
                item.pop('_id')
            client.close()
            print(data)
            self.write({"data": data})

    def post(self):
        if not self.get_secure_cookie('user'):
            self.redirect('/')
        msg = self.get_argument('message')
        name = self.get_argument('name')
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        ip = '.'.join(self.request.remote_ip.split('.')[0:2]) + '.*.*'

        client = mongo_db()
        db = client['message']
        col = db['message']
        data = dict(name=name, msg=msg, dt=dt, ip=ip)
        col.insert_one(data)
        client.close()
        self.redirect('/')


class IndexHandler(BaseHandler):

    def get(self):
        if not self.get_secure_cookie('user'):
            self.redirect('/static/login.html')
        else:
            self.redirect('/static/index.html')


class LoginHandler(BaseHandler):

    def post(self):
        form = json.loads(self.request.body)
        print(form)  # form是字典了
        self.write({'status': 'ok'})

    def get(self):
        data = dict(name='Benny', age=18, family=['China', 'Earch'])
        self.write(data)


class RunServer:
    root_path = os.path.dirname(__file__)
    static_path = os.path.join(root_path, 'static')
    handlers = [
        (r'/message', MessageHandler),
        (r'/login', LoginHandler),
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
