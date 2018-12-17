# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 0017 下午 3:38
# @Author  : 杨宏兵
# @File    : 1.1 实现链表逆转（递归法，不带表头）.py
# @Software: PyCharm
class LNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Link_list():
    def get_link(self, length):
        head = LNode()
        head.data =1
        ptr = head
        i = 2
        while i <= length:
            newNode = LNode()
            newNode.data = i
            ptr.next = newNode
            ptr = ptr.next
            i += 1
        return head

    def print_linklist(self, head):
        if head is None:
            print('列表为空，无法输出')
            return
        ptr = head
        while ptr != None:
            print(ptr.data)
            ptr = ptr.next

    def reverse(self,head):
        if head is None or head.next is None:
            return head
        newhead = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return newhead
if __name__ == "__main__":
    newlist = Link_list()
    head = newlist.get_link(10)
    print('___________逆转之前：_______________')
    newlist.print_linklist(head)
    new_head = newlist.reverse(head)
    print('___________逆转之后：_______________')
    newlist.print_linklist(new_head)



