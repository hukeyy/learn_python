#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys
from conf import settings
from modules import socket_server


BASE_DIR = os.path.dirname(os.getcwd())
sys.path.insert(0, BASE_DIR)

if __name__ == '__main__':
    server = socket_server.socketserver.ThreadingTCPServer(settings.IP_PORT, socket_server.MyServer)
    server.serve_forever()



























