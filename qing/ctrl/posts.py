# -*- coding: utf-8 -*-

import web
import markdown
from settings import render_template
from ctrl.utils import login_required
from models import Post

class PostList:
    @login_required
    def GET(self):
        context = web.ctx.request
        uid = web.ctx.session.uid
        posts = web.ctx.orm.query(Post).filter(Post.user_id==int(uid)).order_by('posts.id DESC')
        context['posts'] = posts

        return render_template("posts/list.html", **context)

class AddPost:
    @login_required
    def GET(self):
        context = web.ctx.request
        return render_template("posts/addpost.html", **context)

    def POST(self):
        i = web.input()
        title = i.title
        content = i.content
        #content_html = markdown.markdown(content)
        post = Post(user_id=int(web.ctx.session.uid), title=title, content=content)
        web.ctx.orm.add(post)
        web.ctx.orm.commit()

        raise web.seeother(post.get_absolute_url)

class SignPost:
    def GET(self, pid):
        context = web.ctx.request
        post = web.ctx.orm.query(Post).filter(Post.id==int(pid)).first()

        context['post'] = post
        return render_template("posts/sign_post.html", **context)


