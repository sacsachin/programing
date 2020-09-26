# !/usr/bin/python3

"""
"""
from collections import deque

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

def solve(head):
    nodes = deque()
    current = head

    while current:
        nodes.append(current.val)
        current = current.next

    current = head
    ans = []
    left = True
    while current:
        if left:
            current.val = nodes.popleft()
        else:
            current.val = nodes.pop()
        left = not left
        ans.append(current.val)
        current = current.next

    return ans[::]

if __name__ == "__main__":
    ll = LinkList([(lambda x: int(x))(x) for x in input().split()])
    print(solve(ll.head))
