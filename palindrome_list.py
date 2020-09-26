# !/usr/bin/python3

"""
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

def solve(head):
    temp = head
    n = 0
    while temp is not None:
        n += 1
        temp = temp.next
    temp = head
    prev = None
    for i in range(n//2):
        prev = temp
        temp = temp.next
    prev.next = None
    if n%2 ==1: temp=temp.next
    current = temp
    prev = None
    while current is not None:
        node = current.next
        current.next = prev
        prev = current
        current = node
    temp = prev
    while temp is not None and head is not None:
        if temp.val != head.val:
            return False
        temp = temp.next
        head = head.next
    return True

if __name__ == "__main__":
    ll = LinkList([(lambda x: int(x))(x) for x in input().split()])
    print(solve(ll.head))
