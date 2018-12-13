# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 0013 下午 1:34
# @Author  : 杨宏兵
# @File    : 8.7 堆栈排序.py
# @Software: PyCharm


def heap_ajust(lists, position, size):
    top = position
    lchild = 2*position + 1
    rchild = 2*position + 2
    if position < size//2:
        if lchild < size and lists[lchild] > lists[top]:
            top = lchild
        if rchild < size and lists[rchild] > lists[top]:
            top = rchild
        if top != position:
            lists[top], lists[position] = lists[position], lists[top]
            heap_ajust(lists, top, size)
    return lists


def heap_sort(lists):
    size = len(lists)
    if size <= 1:
        return lists
    for i in range(size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        heap_ajust(lists, 0, i)
    return lists


def build_heap(lists):
    size = len(lists)
    for i in range(0, size//2)[::-1]:
        heap_ajust(lists, i, size)


if __name__ == "__main__":
    lists = [3, 4, 2, 8, 9, 5, 1]
    print('__________排序前：_____________')
    print(lists)
    print('__________排序后:_____________')
    build_heap(lists)
    print(heap_sort(lists))
