#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/10/2

"""直接插入排序"""


def straight_insert_sort(seq):
    N = len(seq)
    for i in range(1, N):
        if seq[i] < seq[i-1]:
            temp = seq.pop(i)
            j = 0
            while temp > seq[j]:
                j += 1
            seq.insert(j, temp)

    return seq

if __name__ == '__main__':
    from random import seed, sample
    seed(1)  # 确保每次随即得到的数列不变
    origin = sample(range(100), 20)
    print('origin => ', origin)
    result = straight_insert_sort(origin)
    print('ordered => ', result)



