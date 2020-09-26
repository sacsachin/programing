# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/swap-list-nodes-in-pairs/
Swap List Nodes in pairs
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
    # display(head)
    current = head
    n = 0
    while current:
        n += 1
        current = current.next

    if n == 1:
        return lis(head)[::]
    current = head.next
    head.next = current.next
    current.next = head
    head = current

    prev = head.next
    current = head.next.next

    while current:
        current_next = current.next
        if current_next:
            prev.next = current_next
        else:
            break
        next_next = current_next.next
        current_next.next = current
        current.next = next_next
        prev = current
        current = next_next

    return lis(head)[::]

if __name__ == "__main__":
    ll = LinkList([(lambda x: int(x))(x) for x in input().split()])
    print(solve(ll.head))
