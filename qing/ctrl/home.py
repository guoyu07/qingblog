import web

class Home:
    def GET(self):
        return "home" + str(web.ctx.session.login)
