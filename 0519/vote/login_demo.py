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

USERNAME = 'Benny'
PASSWORD = '$pbkdf2-sha256$29000$WksJ4bzX.p8zpnTOWYsxJg$bZFrCxJb3/jIoOc734jexuxFe9K2vwm/H6/Q2xRzBfQ'
enable_pretty_logging()


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass


class IndexHandler(BaseHandler):
    def get(self):
        # TODO: Training #1 fake cookies, csrf
        ckv = self.get_cookie('isLogin')
        if ckv:
            self.render('welcome.html', username=USERNAME)
        else:
            logging.info('No cookie is present.')
            self.render('index.html', message=None)

    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if username == 'Benny' and pbkdf2_sha256.verify(password, PASSWORD):
            logging.info('Correct username and password.')
            # TODO: Training #1 fake cookies, csrf
            self.set_cookie('isLogin', '1')
            self.render('welcome.html', username=USERNAME)
        else:
            logging.warning('Incorrect username and password')
            self.render('index.html', message='Username or password is incorrect.')


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
