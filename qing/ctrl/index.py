# -*- coding: utf-8 -*-

import web
from settings import render_template

class Index:
    def GET(self):
        render_template("index.html")

