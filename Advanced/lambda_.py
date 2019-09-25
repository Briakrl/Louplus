#!/usr/bin/env python3

pp = [('Leborn James', 98), ('Kevin Durant', 97), ('James Harden', 96), ('Stephen Curry', 95), ('Anthony Davis', 94)]

newlist = sorted(map(lambda i: i[0].upper(), pp), reverse = True)

print(newlist)
