# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/
Remove dyplicate from sorted list ||.
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

def solve(head):
    prev_prev = None
    prev = head
    current = head.next

    display(head)
    while current:
        if current.val != prev.val:
            prev_prev = prev
            prev = current
            current = current.next
        else:
            while current  and current.val == prev.val:
                prev = current
                current = current.next
            if prev_prev != None: prev_prev.next = current
            if prev_prev == None: head = current
            prev = current
            if current: current = current.next
    # if prev_prev == None: head = None
    current = head
    ans = []
    while current:
        ans.append(current.val)
        current = current.next

    return ans[::]

if __name__ == "__main__":
    ll = LinkList([(lambda x: int(x))(x) for x in input().split()])
    print(solve(ll.head))
