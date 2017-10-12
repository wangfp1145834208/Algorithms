#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/10/9


"""
快速排序使用到了递归，每次递归的结果是通过一个基准数将序列分割成两个部分，
其中左半部分的数字皆小于基准数，右半部分的数字皆大于基准数；
直到每个部分只剩下一个数字时开始返回。
"""


def partition(seq, low, high):
    # 每次都使用序列的第一个数字作为基准数
    key = seq[low]
    while low < high:
        while low < high and seq[high] >= key:
            high -= 1
        # 将较小的数字移到左边
        seq[low] = seq[high]
        while low < high and seq[low] <= key:
            low += 1
        # 将较大的数字移到右边
        seq[high] = seq[low]
        seq[low] = key
    # 返回low作为下次递归时的边界
    return low


def quick_sort(seq, low, high):
    if low < high:
        mid = partition(seq, low, high)
        quick_sort(seq, low, mid-1)
        quick_sort(seq, mid+1, high)
    return seq


if __name__ == '__main__':
    from random import seed, sample
    seed(1)  # 确保每次随即得到的数列不变
    origin = sample(range(100), 20)
    print('origin => ', origin)
    result = quick_sort(origin, 0, len(origin)-1)
    print('ordered => ', result)
