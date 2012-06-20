# -*- coding: utf-8 -*-

import random
import hashlib

def gen_sha1(string, salt=None):
    """用于生成激活码"""

    if not salt:
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]

    hash = hashlib.sha1(salt+str(string)).hexdigest()

    return hash

de hash_password(password):
    """密码生成"""

    return str(hashlib.sha1(password+'572').hexdigest())

def check_password(db_pw, in_pw):
    """密码判断"""

    inp = hash_password(in_pw)
    return db_pw == inp

