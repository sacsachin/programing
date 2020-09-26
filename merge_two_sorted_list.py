
# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/remove-duplicates-from-sorted-list/
Remove dyplicate from sorted list.
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

def solve(first, second):
    ans = []
    head = tail = None
    while first and second:
        if first.val <= second.val:
            node = first
            first = first.next
        else:
            node = second
            second = second.next

        if head == None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    while first:
        tail.next = first
        tail = first
        first = first.next
    while second:
        tail.next = second
        tail = second
        second = second.next

    current = head
    while current:
        ans.append(current.val)
        current = current.next
    return ans


if __name__ == "__main__":
    first = LinkList([(lambda x: int(x))(x) for x in input().split()])
    second = LinkList([(lambda x: int(x))(x) for x in input().split()])
    print(solve(first.head, second.head))
