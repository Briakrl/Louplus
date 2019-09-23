#!/usr/bin/env python3

filename = '/home/shiyanlou/shiyanlou.txt'
with open(filename) as file1:
    for num, line in enumerate(file1.readlines()):
        with open('/home/shiyanlou/shiyanlou_copy.txt', 'a') as file2:
            file2.write("{} {}".format(num+1, line))
