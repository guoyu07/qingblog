# -*- coding: utf-8 -*-

import web
from settings import render_template

class Register:
    def GET(self):
        return render_template("auth/reg.html")
