# -*- coding: utf-8 -*-
# Author: hkey
import os


class Manage_cmd(object):
    def cmd(self):
        while True:
            cmd = input('>>>').strip()
            if not cmd: continue
            if hasattr(self, cmd):
                func = getattr(self, 'ls')
                func()
            else:
                print('-bash: %s: command not found' % cmd)

    def ls(self):
        current_file = os.listdir('.')
        print(current_file)


cmd_exec = Manage_cmd()
cmd_exec.cmd()
