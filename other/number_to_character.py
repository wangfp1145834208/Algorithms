#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: wangfp time:2017/10/22


class Num2chr:
    alpha2chr = dict(zip(range(1, 27), 'abcdefghijklmnopqrstuvwxyz'))

    def __init__(self, number):
        self.number = number
        # 存储得到的有效数值
        self.cache = {}
        # 保证每个有效数值的唯一性
        self.count = 1
        self.outer = {}

    # 主程序
    def start(self):
        self.cache[1] = []
        self.valid(self.number, 1)
        self.change()
        self.display()

    # 获取所有有效数值
    # 基本思路是每次增加下一个数字时判断下一个两位数数字的大小
    # 若下一个两位数大于26，则不进行任何操作
    # 若下一个两位数小于等于26，则在cache中创建一个新建，并复制相关数据
    # 尚未处理0...
    def valid(self, num, c_n):
        if len(num) == 1:
            self.cache[c_n].append(num)
            return None
        if len(num) == 0:
            return None
        self.cache[c_n].append(num[0])
        if int(num[:2]) <= 26 and int(num[:2]) != 0:
            self.count += 1
            self.cache[self.count] = self.cache[c_n][:-1] if self.cache[c_n] else []
            self.cache[self.count].append(num[:2])
            self.valid(num[2:], self.count)
        self.valid(num[1:], c_n)

    # 将数字转变为字母
    def change(self):
        for c, values in self.cache.items():
            # outer = [chr(int(v)+96) for v in values]
            outer = [self.alpha2chr[int(v)] for v in values if int(v) != 0]
            self.outer[c] = ''.join(outer)

    # 输出
    def display(self):
        print('原数字为：', self.number)
        print('-'*40)
        fmt = '{:20}{:10}'
        print(fmt.format('有效数值', '最终结果'))
        for i in range(1, self.count+1):
            print(fmt.format('-'.join(self.cache[i]), self.outer[i]))


if __name__ == '__main__':
    number = input('请输入数字：')
    n = Num2chr(number)
    n.start()
