# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 0013 下午 2:57
# @Author  : 杨宏兵
# @File    : 8.8 基数排序.py
# @Software: PyCharm
import math


def radix_sort(lists, radix=10):
    k = math.ceil(math.log(max(lists), radix))
    for i in range(1, k+1):
        bucket = [[] for i in range(radix)]
        for j in lists:
            bucket[int(j//radix**(i-1) % radix)].append(j)
        lists = [j for i in bucket for j in i]
    return lists


if __name__ == "__main__":
    lists = [3, 4, 2, 8, 9, 5, 11, 123, 4331, 123454 ]
    print('__________排序前：_____________')
    print(lists)
    print('__________排序后:_____________')
    print(radix_sort(lists))