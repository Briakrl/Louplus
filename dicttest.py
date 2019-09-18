#!/usr/bin/env python3

import sys

a = {}

for x in sys.argv[1:]:
    a_list = x.split(':')
    key, value = a_list
    a[key] = value

for key, value in a.items():
    print("ID:{} Name:{}".format(key, value))
