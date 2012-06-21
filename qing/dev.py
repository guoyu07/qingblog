# -*- coding: utf-8 -*-
"""
调试工具
"""

from sqlalchemy.orm import scoped_session, sessionmaker

from settings import engine

ctx = scoped_session(sessionmaker(bind=engine))
