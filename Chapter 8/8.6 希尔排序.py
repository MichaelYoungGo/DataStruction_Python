# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 0012 下午 7:12
# @Author  : 杨宏兵
# @File    : 8.6 希尔排序.py
# @Software: PyCharm
def shell_sort(lists):
    lens = len(lists)
    step = 2
    group = len(lists) // 2
    while group > 0:
        for i in range(0, lens):
            j = i + group
            while j < lens:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group], lists[k]= lists[k], key
                    k -= group
                j += group
        group //= step
    return lists

if __name__ == "__main__":
    lists = [3, 4, 2, 8, 9, 5, 1]
    print('__________排序前：_____________')
    print(lists)
    print('__________排序后:_____________')
    print(shell_sort(lists))
