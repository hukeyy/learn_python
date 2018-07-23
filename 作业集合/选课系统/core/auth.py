# -*- coding: utf-8 -*-
# Author: hkey
from conf import settings

class Auth(object):
    def __init__(self):
        self.auth_file = settings.auth_db_file

