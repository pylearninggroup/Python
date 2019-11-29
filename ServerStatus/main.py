#!/usr/bin/python
# coding: utf-8

# GameStatus - main.py
# 2018/9/30 20:51

__author__ = "Benny <benny@bennythink.com>"

import os
import logging
from platform import uname

from concurrent.futures import ThreadPoolExecutor
from tornado import web, ioloop, httpserver, gen, options
from tornado.concurrent import run_on_executor


class BaseHandler(web.RequestHandler):
    executor = ThreadPoolExecutor(10)

    def data_received(self, chunk):
        pass


class IndexHandler(BaseHandler):
    def get(self):
        self.redirect('/static/pages/index.html')


class LoginHandler(BaseHandler):

    @run_on_executor()
    def run_post(self):
        pass

    @gen.coroutine
    def post(self):
        resp = yield self.run_post()
        self.write(resp)


class GameStatusHandler(BaseHandler):

    @run_on_executor()
    def run_get(self):
        pass

    @run_on_executor()
    def run_post(self):
        pass

    @gen.coroutine
    def get(self):
        resp = yield self.run_get()
        self.write(resp)

    @gen.coroutine
    def post(self):
        resp = yield self.run_post()
        self.write(resp)


class WebStatusHandler(BaseHandler):
    @run_on_executor()
    def run_get(self):
        pass

    @run_on_executor()
    def run_post(self):
        pass

    @gen.coroutine
    def get(self):
        resp = yield self.run_get()
        self.write(resp)

    @gen.coroutine
    def post(self):
        resp = yield self.run_post()
        self.write(resp)


class SSStatusHandler(BaseHandler):
    @run_on_executor()
    def run_get(self):
        pass

    @run_on_executor()
    def run_post(self):
        pass

    @gen.coroutine
    def get(self):
        resp = yield self.run_get()
        self.write(resp)

    @gen.coroutine
    def post(self):
        resp = yield self.run_post()
        self.write(resp)


class RunServer:
    root_path = os.path.dirname(__file__)
    page_path = os.path.join(root_path, 'pages')

    handlers = [(r'/', IndexHandler),
                (r'/api/game', GameStatusHandler),
                (r'/api/web', WebStatusHandler),
                (r'/api/ss', SSStatusHandler),
                (r'/api/login', LoginHandler),
                (r'/static/(.*)', web.StaticFileHandler, {'path': root_path}),
                ]
    settings = {
        "static_path": os.path.join(root_path, "static"),
        "cookie_secret": "5Li05DtnQewDZqpmDVB3HAAhFqUu2vDnUSnqezkeu+M=",
        "xsrf_cookies": False,
        "autoreload": True
    }

    application = web.Application(handlers, **settings)

    @staticmethod
    def run_server(port=8888, host='127.0.0.1', **kwargs):
        tornado_server = httpserver.HTTPServer(RunServer.application, **kwargs)
        tornado_server.bind(port, host)

        if uname()[0] == 'Windows':
            tornado_server.start()
        else:
            tornado_server.start(None)

        try:
            print(f'Server is running on http://{host}:{port}')
            ioloop.IOLoop.instance().current().start()
        except KeyboardInterrupt:
            ioloop.IOLoop.instance().stop()
            print('"Ctrl+C" received, exiting.\n')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    options.define("p", default=8888, help="running port", type=int)
    options.define("h", default='127.0.0.1', help="listen address", type=str)
    options.parse_command_line()
    p = options.options.p
    h = options.options.h
    RunServer.run_server(port=p, host=h)
