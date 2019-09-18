#!/usr/bin/env python3

import sys

ouput_dict = {}

def handle_data(x):
    a_list = x.split(":")
    key1, value1 = a_list
    output_dict[key] = value1

def print_data(key2, value2):
    print("ID:{} Name:{}".format(key2, value2))


if __name__ == '__main__':

    for arg in sys.argv[1:]:
        handle_data(arg)

    for key in ouput_dict:
        print_data(key, output_dict[key])
