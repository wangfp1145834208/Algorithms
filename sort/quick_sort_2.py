#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/10/12


def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    key = seq[0]
    big = quick_sort([i for i in seq[1:] if i >= key])
    small = quick_sort([i for i in seq[1:] if i <= key])
    return small + [key] + big


if __name__ == '__main__':
    from random import seed, sample
    seed(1)  # 确保每次随即得到的数列不变
    origin = sample(range(100), 20)
    print('origin => ', origin)
    result = quick_sort(origin)
    print('ordered => ', result)
