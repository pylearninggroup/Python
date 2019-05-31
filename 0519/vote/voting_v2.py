# coding: utf-8
# scripts - login.py
# 2019/3/28 15:03


import os
import platform

from tornado.log import enable_pretty_logging
from concurrent.futures import ThreadPoolExecutor
from tornado import web, ioloop, httpserver, gen
from tornado.concurrent import run_on_executor

enable_pretty_logging()
NAMES = {
    'cc': 0,
    'wxm': 0,
    'byf': 0,
    'lmx': 0,
    'xcq': 0,
    'mjw': 0,
    'wjc': 0
}


class BaseHandler(web.RequestHandler):
    def data_received(self, chunk):
        pass


class IndexHandler(BaseHandler):
    executor = ThreadPoolExecutor(max_workers=20)

    @run_on_executor
    def run_request(self):
        if self.request.method == 'GET':
            return self.render_string('name.html', names=NAMES)
        elif self.request.method == 'POST':
            name = self.get_argument('name')
            NAMES[name] = NAMES[name] + 1

    @gen.coroutine
    def get(self):
        res = yield self.run_request()
        self.write(res)

    @gen.coroutine
    def post(self):
        yield self.run_request()
        return self.redirect('/')


if __name__ == "__main__":
    port = 5022
    host = '0.0.0.0'
    root_path = os.path.dirname(__file__)
    settings = dict(
        template_path=os.path.join(root_path, "templates"),
        cookie_secret="61oETzKXabcddkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    )
    handlers = [(r"/", IndexHandler)]

    application = web.Application(handlers, **settings)

    tornado_server = httpserver.HTTPServer(application)
    tornado_server.bind(port, host)

    if platform.uname()[0] == 'Windows':
        tornado_server.start()
    else:
        tornado_server.start(None)

    try:
        print('Server is running.')
        ioloop.IOLoop.instance().current().start()
    except KeyboardInterrupt:
        ioloop.IOLoop.instance().stop()
        print('"Ctrl+C" received, exiting.\n')
