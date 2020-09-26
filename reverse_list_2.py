# !/usr/bin/pyton3

"""
https://www.interviewbit.com/problems/reverse-link-list-ii/
Reverse List 2.
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

def solve(head, start, end):
    current = head
    n = 0

    stack = []
    index = 0
    while current:
        index += 1
        if index >= start and index <= end:
            stack.append(current.val)
        current = current.next

    current = head
    index = 0
    while stack:
        index += 1
        if index >= start and index <=end:
            current.val = stack.pop()
        current = current.next

    return lis(head)[::]

if __name__ == "__main__":
    ll = LinkList([(lambda x: int(x))(x) for x in input().split()])
    start = int(input())
    end = int(input())
    print(solve(ll.head, start, end))
