#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

from urls import urls

app = web.application(urls, globals(), autoreload=True)

if __name__ == '__main__':
    app.run()
