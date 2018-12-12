# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 0012 下午 3:55
# @Author  : 杨宏兵
# @File    : 8.4 归并排序.py
# @Software: PyCharm
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(lists):
    lens = len(lists)
    if lens <= 1:
        return lists
    num = int(lens/2)
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)


if __name__ == "__main__":
    lists = [3, 4, 2, 8, 9, 5, 1]
    print('__________排序前：_____________')
    print(lists)
    print('__________排序后:_____________')
    print(merge_sort(lists))

