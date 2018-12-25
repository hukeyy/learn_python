#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys
from conf import settings

BASE_DIR = os.path.join(os.getcwd())

sys.path.insert(0, BASE_DIR)

from modules import socket_server

if __name__ == '__main__':
    server = socket_server.socketserver.ThreadingTCPServer((settings.IP_PORT), socket_server.MyServer)
    server.serve_forever()


























