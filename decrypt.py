#!/usr/bin/env python3

with open('output.txt', 'rb') as f:
    out = f.read()

out = bytes.fromhex(out)

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'break it'
]


def recurse(out, random_strs, list, index):
    for i in range(5 - index):
        recurse(out, random_strs, list, i)
