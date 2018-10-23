#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
import pickle

with open('school', 'rb') as f:
    data = pickle.load(f)

print(data)