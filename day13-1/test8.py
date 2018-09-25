#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey

import os


def search(target):
    while True:
        PATH = yield
        for top_dir, dir, files in os.walk(PATH):
            for file in files:
                target.send(os.path.join(top_dir, file))


def opener(target, pattern=None):
    while True:
        file_path = yield
        with open(file_path, encoding='utf-8') as f:
            target.send((file_path, f))


def cat(target):
    while True:
        filepath, f = yield
        for line in f:
            tag = target.send((filepath, line))
            if tag:
                break


def grep(target, pattern):
    tag = False
    while True:
        filepath, line = yield tag


