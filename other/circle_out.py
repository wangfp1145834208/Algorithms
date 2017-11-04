#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/10/17


def out(seq, m, start=-1):
    N = len(seq)
    if N < m:
        return seq

    pop_list = [] if start < 0 else [start]
    if start >= 0:
        print(seq[start])
    while 1:
        start += m
        if start < N:
            print(seq[start])
            pop_list.append(start)
        else:
            break
    for i in pop_list[::-1]:
        seq.pop(i)
    return out(seq, m, start=start - N)


def circle_out(n, m):
    seq = list(range(1, n+1))
    left = out(seq, m)
    return left


if __name__ == '__main__':
    result = circle_out(10, 3)
    print('最终剩余数字：', result)
