# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 0014 下午 5:03
# @Author  : 杨宏兵
# @File    : 1.1 实现链表的逆转.py
# @Software: PyCharm


class LNode:
    def __init__(self):
        self.data = None
        self.next = None


def Biuld_link(size):
    head = LNode()
    ptr = head
    for i in range(1, size):
        New_LNode = LNode()
        New_LNode.data = i
        ptr.next = New_LNode
        ptr = ptr.next
    return head


def reverse(head):
    if head == None or head.next == None:
        return
    pre = None
    cur = head.next
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        head.next = cur
        cur = tmp
    return head




def print_link(head):
    ptr = head.next
    while ptr != None:
        print(ptr.data)
        ptr = ptr.next


if __name__ == '__main__':
    head = Biuld_link(10)
    print("-----------链表反转之前：--------------")
    print_link(head)
    head = reverse(head)
    print("-----------链表反转之后：--------------")
    print_link(head)
