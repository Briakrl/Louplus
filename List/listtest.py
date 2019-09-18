#!/usr/bin/env python3

import sys

a = []
b = []

for i in sys.argv[1:]:
    if len(i) > 3:
        a.append(i)
    else:
        b.append(i)

print(' '.join(b))
print(' '.join(a))
