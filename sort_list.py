# !/usr/bin/python3

"""
https://leetcode.com/problems/sort-list/
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


if __name__ == "__main__":
    ll = LinkList(list(map(int, input().split())))
    print(solve(ll.head))
