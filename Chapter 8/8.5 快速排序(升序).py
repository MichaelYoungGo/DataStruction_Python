# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 0012 下午 5:47
# @Author  : 杨宏兵
# @File    : 8.5 快速排序(升序).py
# @Software: PyCharm


def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    hight = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left-1)
    quick_sort(lists, left+1, hight)
    return lists


if __name__ == "__main__":
    lists = [3, 4, 2, 8, 9, 5, 1]
    print('__________排序前：_____________')
    print(lists)
    print('__________排序后:_____________')
    print(quick_sort(lists, 0, len(lists)-1))

