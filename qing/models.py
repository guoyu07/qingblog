# -*- coding: utf-8 -*-

import datetime

import web

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref

from settings import engine

def load_sqla(handler):
    web.ctx.orm = scoped_session(sessionmaker(bind=engine))
    try:
        return handler()
    except web.HTTPError:
        web.ctx.orm.commit()
        raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()
        web.ctx.orm.close()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.datetime.now)
    actived = Column(Boolean, default=False)

    def __repr__(self):
        return '<User ("%s")>' % self.email

class UserSignup(Base):
    __tablename__ = 'user_signup'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    active_key = Column(String)
    user = relationship("User", backref=backref("user_signup", uselist=False))

    def _repr__(self):
        return "<UserSignup (%s)>" % str(self.id)

class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    username = Column(String, unique=True)
    comefrom = Column(String)
    jj = Column(Text)
    user = relationship("User", backref=backref('profiles', uselist=False))

    def __repr__(self):
        return '<Profile <%d: "%s">' % (self.user_id, self.username)

users_table = User.__table__
user_signup_table = UserSignup.__table__
profiles_table = Profile.__table__

metadata = Base.metadata

if __name__ == '__main__':
    metadata.create_all(engine)



