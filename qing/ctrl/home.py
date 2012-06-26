import web

## class Index:
##     def GET(self):
##         if web.ctx.session.login == 1:
##             raise web.seeother("/home")

class Home:
    def GET(self):
        return "home" + str(web.ctx.session.login)+web.ctx.session.username
