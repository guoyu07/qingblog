# -*- coding: utf-8 -*-

urls = (
    '/', 'ctrl.index.Index',
    #auth
    '/auth/login', 'ctrl.auth.Login',
    '/auth/setpo', 'ctrl.auth.SetProfile',
    '/auth/logout', 'ctrl.auth.Logout',
    '/auth/reg', 'ctrl.auth.Register',
    '/auth/succ', 'ctrl.auth.Succ',
    '/auth/active/(?P<uid>\d+)/(?P<ac_key>\w+)', 'ctrl.auth.Active',
    '/home', 'ctrl.home.Home',
    #posts
    '/posts/add', 'ctrl.posts.AddPost',
    )
