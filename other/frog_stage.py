#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/11/4

"""
yield的生成器拥有许多优秀的性质，需要去深入探索
充分使用生成器的可迭代性，可以使得程序的编写简练很多
"""


def frog_stage(num):
    stage = '0' * num

    def method(left=stage):
        if len(left) <= 1:
            yield (left,) if len(left) == 1 else ()
        else:
            for result in method(left[1:]):
                yield (left[0],) + result
            for result in method(left[2:]):
                yield (left[:2],) + result

    count = 0
    for i in method():
        count += 1
        print('-'.join(i))
    print('总共%d种可能' % count)


def fib(n):
    return n if n <= 2 else fib(n-1) + fib(n-2)


if __name__ == '__main__':
    stage_num = int(input('输入台阶数目：'))
    frog_stage(stage_num)
    f = fib(stage_num)
    print('应该有%d种可能' % f)
