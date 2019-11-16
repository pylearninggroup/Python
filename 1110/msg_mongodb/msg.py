# coding: utf-8
# course - msg.py
# 2019/9/15 12:49


import logging
import time
from platform import uname

from tornado import web, ioloop, httpserver, options

import pymongo


class BaseHandler(web.RequestHandler):
    def data_received(self, chunk):
        pass


def mongo_db():
    client = pymongo.MongoClient()
    return client


class IndexHandler(BaseHandler):

    def get(self):
        client = mongo_db()
        db = client['demo']
        col = db['msg']
        data = col.find()

        comments = []
        for item in data:
            line = "姓名：{} 留言：{} 时间：{} IP：{}".format(item['name'], item['msg'],
                                                    item['dt'], item['ip'])
            comments.append(line)
        client.close()
        self.render('main.html', message=comments)

    def post(self):
        msg = self.get_argument('message')
        name = self.get_argument('name')
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        ip = '.'.join(self.request.remote_ip.split('.')[0:2]) + '.*.*'

        client = mongo_db()
        db = client['demo']
        col = db['msg']
        data = dict(name=name, msg=msg, dt=dt, ip=ip)
        col.insert_one(data)
        client.close()
        self.redirect('/')


class RunServer:
    handlers = [
        (r'/', IndexHandler),
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
