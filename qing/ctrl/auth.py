# -*- coding: utf-8 -*-

import web
from settings import render_template

from models import User, UserSignup
from ctrl.utils import gen_sha1, hash_password, render_mail

class Register:
    def GET(self):
        if web.ctx.session.login == 1:
            raise web.seeother('/dashboad')

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



class Succ:
    def GET(self):
        return 'succ!'



