#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys

BASE_DIR = os.path.dirname(os.getcwd())
sys.path.insert(0, BASE_DIR)

from modules import socket_server
from conf.settings import IP_PORT


if __name__ == '__main__':
    server = socket_server.socketserver.ThreadingTCPServer((IP_PORT), socket_server.MyServer)
    server.serve_forever()

