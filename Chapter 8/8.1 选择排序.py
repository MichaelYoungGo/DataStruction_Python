# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 0011 下午 5:23
# @Author  : 杨宏兵
# @File    : 8.1 选择排序.py
# @Software: PyCharm


def select_sort(lists):
    lens = len(lists)
    for i in range(0, lens):
        min = i
        for j in range(i + 1, lens):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists

if __name__ == "__main__":
    lists = [3, 4, 2, 8, 9, 5, 1]
    print('__________排序前：_____________')
    print(lists)
    print('__________排序后:_____________')
    print(select_sort(lists))
