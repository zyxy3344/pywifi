# Author:Kali Yu
"""
密码本生成
"""
import itertools as its

words = "1234567890"

r = its.product(words, repeat=6)
with open('pass.txt', 'a')as f:
    for i in r:
        f.write(''.join(i))
        f.write(''.join('\n'))

