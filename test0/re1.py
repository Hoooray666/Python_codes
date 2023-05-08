# -*- coding: utf-8 -*-
from hashlib import md5
from string import digits, ascii_letters, ascii_lowercase, ascii_uppercase, punctuation, whitespace, printable, \
    MyOwnType
from itertools import permutations, product
import sys
import time


def decipher_md5(md5_value: str, plaintext_len: int = 5,
                 plaintext_letter_dict: str = ascii_letters + punctuation, dup: bool = False):
    md5_value = md5_value.lower()
    if len(md5_value) != 32:
        print('\n不是有效的md5散列!')
        sys.exit(-1)

    try:
        if dup:  # 全排列，可重复
            # plaintext_set = [''.join(p) for p in product(punctuation, repeat=plaintext_len)]
            plaintext_set = [''.join(p) for p in product(MyOwnType, repeat=plaintext_len)]
            # print(plaintext_set)
        else:  # 全排列，不可重复
            plaintext_set = permutations(MyOwnType, plaintext_len)

        for item in plaintext_set:
            item = ''.join(item)
            print(item)

            if md5(item.encode()).hexdigest() == md5_value:
                print('\n成功解出明文: ' + md5_value + ' ==> ' + item)
                break

        if md5(item.encode()).hexdigest() != md5_value:
            sys.exit(1)

    except SystemExit:
        print('\n解析失败，请检查下给定的明文长度（默认 plaintext_len: int = 4）!!!')


def test():
    decipher_md5(md5_value='b5a5d6911aa48b50139c7122ef05ca9a', plaintext_letter_dict=punctuation, dup=True)


if __name__ == '__main__':
    # test()
    t1 = time.time()
    decipher_md5(md5_value='f8728f24e01c1aaf54e23f7f0d591384', plaintext_letter_dict=ascii_letters)
    t2 = time.time()
    print('using time: '+(t2-t1)+'s')