# -*- coding: utf-8 -*-

import web
from settings import render_template

from models import User, UserSignup, Profile
from ctrl.utils import gen_sha1, hash_password, render_mail, check_password, login_required

class Login:
    def GET(self):
        if web.ctx.session.login == 1:
            raise web.seeother('/home')

    def POST(self):
        i = web.input()
        email = i.email.strip()
        password = i.password

        user = web.ctx.orm.query(User).filter(User.email==email).first()

        if user and user.actived and check_password(user.password, password):
            web.ctx.session.login = 1
            #web.ctx.session.username = user.username
            raise web.seeother('/home')
        else:
            web.ctx.msg = u'帐号不存在或与密码符，请重新核对或该帐号还未激活'
            raise web.seeother('/auth/login')

class Logout:
    @login_required
    def GET(self):
        web.ctx.session.kill()
        web.ctx.session.msg=u"已正常退出，请重新登录"
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
            #web.ctx.session.login = 1
            web.ctx.session.email = email
            web.sendmail(web.config.smtp_username, email, u'注册邮件',
                         render_mail('templates/auth/activation_email_message.txt', **context))

            raise web.seeother('/auth/succ')
        else:
            raise

class CheckEmail:
    def POST(self):
        i = web.input()
        email = i.email.strip()
        user = web.ctx.orm.query(User).filter(User.email==email).first()
        if user:
            ## print 1
            return '1'

class Active:
    def GET(self, uid, ac_key):
        user = web.ctx.orm.query(UserSignup).filter(UserSignup.id==int(uid)).\
               filter(UserSignup.active_key==ac_key).first()
        if user:
            u = web.ctx.orm.query(User).filter(User.id==int(uid)).first()
            u.actived = 1
            user.active_key = '1'
            web.ctx.orm.commit()
            web.ctx.session.uid = uid
            raise web.seeother('/auth/setpo')
        else:
            return 'error'

class SetProfile:
    def GET(self):
        context = {}
        email = web.ctx.session.email
        context['email'] = email
        context['uid'] = web.ctx.session.uid

        return render_template("auth/set_profile.html", **context)

    def POST(self):
        i = web.input()
        username = i.username.strip()
        uid = i.uid
        comefrom = i.comefrom
        jj = i.jj

        user = web.ctx.orm.query(User).filter(User.id==int(uid)).first()

        if user:
            po = Profile(username=username, user_id=user.id, comefrom=comefrom, jj=jj)
            web.ctx.orm.add(po)
            web.ctx.orm.commit()
            web.ctx.session.login = 1
            web.ctx.session.username=username
            raise web.seeother('/home')
        esle:
            web.ctx.msg = u"该帐号已激活过")
            raise web.seeother("/")


class Succ:
    def GET(self):
        context = {}
        context['email'] = web.ctx.session.email

        return render_template("auth/succ.html", **context)

