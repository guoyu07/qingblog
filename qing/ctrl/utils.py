# -*- coding: utf-8 -*-

import random
import hashlib
import web
from jinja2 import Template

def gen_sha1(string, salt=None):
    """用于生成激活码"""

    if not salt:
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]

    hash = hashlib.sha1(salt+str(string)).hexdigest()

    return hash

def hash_password(password):
    """密码生成"""

    return str(hashlib.sha1(password+'572').hexdigest())

def check_password(db_pw, in_pw):
    """密码判断"""

    inp = hash_password(in_pw)
    return db_pw == inp

def render_mail(filename, **context):
    f = open(filename, 'r')
    t = Template(f.read().decode('utf-8'))

    return t.render(**context)

def login_required(func):
    def function(*args):
        if web.ctx.session.login == 0:
            raise web.seeother('/auth/login')
        else:
            return func(*args)
        return function
