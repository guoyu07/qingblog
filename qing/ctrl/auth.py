# -*- coding: utf-8 -*-

import web
from settings import render_template

from models import User, UserSignup
from ctrl.utils import gen_sha1, hash_password, render_mail, check_password, login_required

## def login_required(func):
##     def function(*args):
##         if web.ctx.session.login == 0:
##             raise web.seeother('/auth/login')
##         else:
##             return func(*args)
##         return function

class Login:
    def GET(self):
        if web.ctx.session.login == 1:
            raise web.seeother('/home')

    def POST(self):
        i = web.input()
        email = i.email.strip()
        password = i.password

        user = web.ctx.orm.query(User).filter(User.email==email).first()

        if user and check_password(user.password, password):
            web.ctx.session.login = 1
            web.ctx.session.email = user.email
            raise web.seeother('/home')

class Logout:
    @login_required
    def GET(self):
        web.ctx.session.kill()
        raise web.seeother("/auth/login")

class Register:
    def GET(self):
        if web.ctx.session.login == 1:
            raise web.seeother('/home')

        return render_template("auth/reg.html")

    def POST(self):
        context = {}
        i = web.input()
        email = i.email.strip()
        password = i.password
        if not email:
            web.ctx.msg = u"邮箱地址不能为空"
            raise web.seeother('/auth/reg')
        user = User(email=email, password=hash_password(password))
        web.ctx.orm.add(user)
        #web.ctx.orm.commit()

        u = web.ctx.orm.query(User).filter(User.email==email).first()
        if u:
            active_key = gen_sha1(u.email)
            context['active_key'] = active_key
            context['uid'] = u.id
            user_signup = UserSignup(user=u, active_key=active_key)
            web.ctx.orm.add(user_signup)
            web.ctx.orm.commit()
            web.ctx.session.login = 1
            web.ctx.session.email = email
            web.sendmail(web.config.smtp_username, email, u'注册邮件',
                         render_mail('templates/auth/activation_email_message.txt', **context))

            raise web.seeother('/auth/succ')
        else:
            raise

class Active:
    def GET(self, uid, ac_key):
        user = web.ctx.orm.query(UserSignup).filter(UserSignup.id==int(uid)).\
               filter(UserSignup.active_key==ac_key).first()
        if user:
            u = web.ctx.orm.query(User).filter(User.id==int(uid)).first()
            u.actived = 1
            user.active_key = '1'
            web.ctx.orm.commit()
        else:
            return 'error'

class Succ:
    def GET(self):
        context = {}
        context['email'] = web.ctx.session.email

        return render_template("auth/succ.html", **context)


