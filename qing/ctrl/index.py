# -*- coding: utf-8 -*-

import web
from settings import render_template

class Index:
    def GET(self):
        if web.ctx.session.login == 1:
            raise web.seeother("/home")
        return render_template("index.html")

