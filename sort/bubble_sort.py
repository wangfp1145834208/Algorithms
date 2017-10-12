#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/10/2

"""冒泡排序：从后向前两两比较，最终在每次遍历中将剩余部分的最小数字排到剩余部分的开头，
   使用flag用于判断剩余部分的元素是否已经排好顺序，若是，则不需要再比较了"""


def bubble_sort(seq):
    N = len(seq)
    count1 = 0
    count2 = 0
    flag = 0
    for i in range(N):
        if flag:
            break
        flag = 1
        for j in range(N-1, i, -1):
            count1 += 1
            if seq[j-1] > seq[j]:
                count2 += 1
                seq[j-1], seq[j] = seq[j], seq[j-1]
                flag = 0
    print('进行了%d次比较，进行了%d次调换' % (count1, count2))
    return seq

if __name__ == '__main__':
    from random import seed, sample
    seed(1)  # 确保每次随即得到的数列不变
    origin = sample(range(100), 20)
    print('origin => ', origin)
    result = bubble_sort(origin)
    print('ordered => ', result)
