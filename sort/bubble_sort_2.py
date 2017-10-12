#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/10/12


def bubble_sort(seq):
    N = len(seq)
    for i in range(N):
        for j in range(N-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return seq


if __name__ == '__main__':
    from random import seed, sample
    seed(1)  # 确保每次随即得到的数列不变
    origin = sample(range(100), 20)
    print('origin => ', origin)
    result = bubble_sort(origin)
    print('ordered => ', result)
