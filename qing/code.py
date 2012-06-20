#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from urls import urls
from models import load_sqla

if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store, initializer={'login':0, 'username':''})
    web.config._session = session
else:
    session = web.config._session

def session_hook():
    web.ctx.session = session

app = web.application(urls, globals(), autoreload=True)

app.add_processor(web.loadhook(session_hook))
app.add_processor(load_sqla)

if __name__ == '__main__':
    app.run()
