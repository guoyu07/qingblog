import web
from settings import render_template
from ctrl.utils import login_required

## def login_required(func):
##     def function(*args):
##         if web.ctx.session.login == 0:
##             raise web.seeother('/auth/login')
##         else:
##             return func(*args)
##     return function

class AddPost:
    @login_required
    def GET(self):
        return render_template("posts/addpost.html")
756121994
