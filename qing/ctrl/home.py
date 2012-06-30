import web
from settings import render_template
from utils import login_required
from models import Profile

class Home:
    @login_required
    def GET(self):

        context = web.ctx.request
        uid = web.ctx.session.uid
        po = web.ctx.orm.query(Profile).filter(Profile.user_id==int(uid)).first()

        context['username'] = po.username
        web.ctx.session.username = po.username

        return render_template("home.html", **context)
