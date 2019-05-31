# coding: utf-8
# scripts - login.py
# 2019/3/28 15:03


import logging
import time
import os

import tornado.ioloop
import tornado.web
from tornado.log import enable_pretty_logging
from passlib.hash import pbkdf2_sha256

enable_pretty_logging()
FRUITS = {
    'apple': 0,
    'orange': 0,
    'banana': 0,
    'grape': 0}


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass


class IndexHandler(BaseHandler):
    def get(self):
        self.render('fruits.html', fruits=FRUITS)

    def post(self):
        food = self.get_argument('fruits')
        FRUITS[food] = FRUITS[food] + 1
        return self.redirect('/')


def make_app():
    root_path = os.path.dirname(__file__)
    settings = dict(
        template_path=os.path.join(root_path, "templates"),
        # cookie_secret="61oETzKXabcddkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",

    )
    return tornado.web.Application(
        [(r"/", IndexHandler)],
        address="0.0.0.0", **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(5022)
    print('Starting on 0.0.0.0:5022')
    tornado.ioloop.IOLoop.current().start()
