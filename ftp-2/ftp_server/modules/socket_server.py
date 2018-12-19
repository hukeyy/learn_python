#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import os, sys, pickle
from conf import settings
from modules.log import Logger
import socketserver


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                auth_info = self.request.recv(1024)
                
            except ConnectionResetError as e:
                print('Error:', e)
                break
            

























