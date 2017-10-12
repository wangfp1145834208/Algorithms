#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/10/12


"""插入排序：每次遍历序列的前1（2、3、4...）个部分，并进行排序"""


def insert_sort(seq):
    length = len(seq)
    for i in range(length):
        for j in range(i, 0, -1):  # 这部分就相当于冒泡排序
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]

    return seq

if __name__ == '__main__':
    from random import seed, sample
    seed(1)  # 确保每次随即得到的数列不变
    origin = sample(range(100), 20)
    print('origin => ', origin)
    result = insert_sort(origin)
    print('ordered => ', result)
