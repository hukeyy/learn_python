#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: hkey
# print(1 > 1 or 3 > 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# 1 > 1 or 3 > 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# 1 > 1 or 3 > 4 or F and 9 > 8 or 7 < 6
# 1 > 1 or 3 > 4 or F or 7 < 6
# F or F or 7 < 6
# F or 7 < 6
# F

# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# F and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# F or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
# F or F and 9 > 8 or 7 < 6
# F or F or 7 < 6
# F or 7 < 6
# F

# print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8 and 4 > 6 or 3 < 2)
# 1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8 and 4 > 6 or 3 < 2
# F or 4 > 5 and 2 > 1 or 9 < 8 and 4 > 6 or 3 < 2
# F or F or 9 < 8 and 4 > 6 or 3 < 2
# F or F or F or 3 < 2
# F or F or 3 < 2
# F or 3 < 2
# F

# print(8 or 3 and 4 or 2 and 0 or 9 and 7)
# 8 or 3 and 4 or 2 and 0 or 9 and 7
# 8 or 4 or 0 or 7
# 8 or 0 or 7
# 8 or 7
# 8

# print(0 or 2 and 3 and 4 or 6 and 0 or 3)
# 0 or 2 and 3 and 4 or 6 and 0 or 3
# 0 or 3 and 4 or 6 and 0 or 3
# 0 or 4 or 6 and 0 or 3
# 0 or 4 or 0 or 3
# 4 or 0 or 3
# 4 or 3
# 4

# print(5 and 9 or 10 and 2 or 3 and 5 or 4 or 5)
# 5 and 9 or 10 and 2 or 3 and 5 or 4 or 5
# 9 or 10 and 2 or 3 and 5 or 4 or 5
# 9 or 2 or 3 and 5 or 4 or 5
# 9 or 2 or 5 or 4 or 5
# 9 or 5 or 4 or 5
# 9 or 4 or 5
# 9 or 5
# 9

print(6 or 2 > 1)
# 6 or 2 > 1
# 6 or T
# 6

print(3 or 2 > 1)
# 3 or 2 > 1
# 3 or T
# 3

print(0 or 5 < 4)
# 0 or 5 < 4
# 0 or F
# False

print(5 < 4 or 3)
# 5 < 4 or 3
# F or 3
# 3

print(2 > 1 or 6)
# 2 > 1 or 6
# T or 6
# T

print(3 and 2 > 1)
# 3 and 2 > 1
# 3 and T
# T

print(0 and 3 > 1)
# 0 and 3 > 1
# 0 and T
# 0

print(2 > 1 and 3)
# 2 > 1 and 3
# T and 3
# 3

print(3 > 1 and 0)
# 3 > 1 and 0
# T and 0
# 0

print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)
# 3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2
# T and 2 or 2 < 3 and 3 and 4 or 3 > 2
# 2 or 2 < 3 and 3 and 4 or 3 > 2
# 2 or F and 3 and 4 or 3 > 2
# 2 or F and 4 or 3 > 2
# 2 or F or 3 > 2
# 2 or 3 > 2
# 2 or T
# 2



