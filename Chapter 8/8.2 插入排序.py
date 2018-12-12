# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 0011 下午 6:00
# @Author  : 杨宏兵
# @File    : 8.2 插入排序.py
# @Software: PyCharm


def insert_sort(lists):
    lens = len(lists)
    for i in range(1, lens):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j+1], lists[j] = lists[j], key
            j -= 1
        i += 1
    return lists

if __name__ == "__main__":
    lists = [3, 4, 2, 8, 9, 5, 1]
    print('__________排序前：_____________')
    print(lists)
    print('__________排序后:_____________')
    print(insert_sort(lists))
