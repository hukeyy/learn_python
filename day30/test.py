#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import os, subprocess

# print('12312'.isdigit())

result = subprocess.run('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(result.stdout.read())























