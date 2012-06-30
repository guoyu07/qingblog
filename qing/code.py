#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from urls import urls
from settings import load_sqla

app = web.application(urls, globals(), autoreload=True)

if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'login':0, 'username':''})
    web.config._session = session
else:
    session = web.config._session

def session_hook():
    web.ctx.session = session

def request_hook():
    request = {}
    request['user'] = web.ctx.session.username
    web.ctx.request = request

app.add_processor(web.loadhook(session_hook))
app.add_processor(load_sqla)
app.add_processor(web.loadhook(request_hook))

if __name__ == '__main__':
    app.run()
