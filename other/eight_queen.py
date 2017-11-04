#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/11/4


def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        # 判断冲突——同一列或对角线上
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            # 若是最后一个皇后，并且位置与之前的皇后不冲突
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyp(solution):
    def line(pos, length=len(solution)):
        return '.'*pos + 'X' + '.'*(length-pos-1)
    for pos in solution:
        print(line(pos))


if __name__ == '__main__':
    # import random
    #
    # prettyp(random.choice(list(queens())))
    for result in queens():
        print(result)
