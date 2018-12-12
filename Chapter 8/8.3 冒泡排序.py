# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 0012 下午 3:27
# @Author  : 杨宏兵
# @File    : 8.3 冒泡排序.py
# @Software: PyCharm


def bubble_sort(lists):
    lens = len(lists)
    for i in range(0, lens):
        for j in range(lens-1, i, -1):
            if lists[j-1] > lists[j]:
                lists[j-1], lists[j] = lists[j], lists[j-1]
    return lists

if __name__ == "__main__":
    lists = [3, 4, 2, 8, 9, 5, 1]
    print('__________排序前：_____________')
    print(lists)
    print('__________排序后:_____________')
    print(bubble_sort(lists))
