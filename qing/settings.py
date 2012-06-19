# -*- coding: utf-8 -*-

import os
import web
from jinja2 import Environment, FileSystemLoader

web.config.debug = True

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

def render_template(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(
        loader=FileSystemLoader(path('templates')),
        extensions=extensions,
        )

    jinja_env.globals.update(globals)
    return jinja_env.get_template(template_name).render(context)
