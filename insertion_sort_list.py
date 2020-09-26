# !/usr/bin/python3

"""
https://leetcode.com/problems/insertion-sort-list/
Insertion sort list.
"""

class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class LinkList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(val=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(val=elem)
                node = node.next

def display(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print(end="\n")

def lis(head):
    lis = []
    while head:
        lis.append(head.val)
        head = head.next
    return lis[::]

def solve(head):
    current = head
    prev_current = None
    while current:
        mi = Node(float("inf"))
        point = current
        prev = point_prev = None
        while point:
            if point.val < mi.val:
                mi = point
                point_prev = prev
            prev = point
            point = point.next
        if point_prev:
            point_prev.next = mi.next
        if current != mi:
            if prev_current:
                prev_current.next = mi
                mi.next = current
            else:
                head = mi
                mi.next = current
            prev_current = mi
        else:
            prev_current = current
            current = current.next
    return lis(head)[::]

if __name__ == "__main__":
    ll = LinkList([(lambda x: int(x))(x) for x in input().split()])
    print(solve(ll.head))
