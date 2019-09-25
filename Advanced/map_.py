#!/usr/bin/env python3

pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]

def AP(i):
    return i[0].lower()

result_list = map(AP, pp)
newlist = list(result_list)
print(newlist)
