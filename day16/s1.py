# -*- coding: utf-8 -*-
# Author: hkey

Flag = True

while Flag:
    print('level-1')
    choice = input('level-1 >>:').strip()
    if choice == 'quit': Flag = False
    while Flag:
        print('level-2')
        choice = input('level-2 >>:').strip()
        if choice == 'quit': Flag = False
        while Flag:
            print('level-3')
            choice = input('level-3 >>:').strip()
            if choice == 'quit': Flag=False