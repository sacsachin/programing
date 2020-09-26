# !/usr/bin/python3

"""
https://leetcode.com/problems/partition-list/
Partition List
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

def solve(head, x):
    current = head
    first = current_first = None
    second = current_second = None

    while current:
        if current.val < x:
            if first == None:
                first = current_first = current
            else:
                current_first.next = current
                current_first = current_first.next
            current = current.next
            current_first.next = None

        else:
            if second == None:
                second = current_second = current
            else:
                current_second.next = current
                current_second = current_second.next
            current = current.next
            current_second.next = None
    # display(first)
    # display(second)

    if current_first:
        current_first.next = second
        head = first
    else:
        head = second

    return lis(head)[::]

if __name__ == "__main__":
    ll = LinkList(list(map(int, input().split())))
    x = int(input())
    print(solve(ll.head, x))
