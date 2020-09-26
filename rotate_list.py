
# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/rotate-list/
Rotate List.
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

def solve(head, pos):
    ans = []
    current = head
    n = 0
    while current:
        n += 1
        if current.next == None:
            last = current
        current = current.next

    if n == 1:
        return [head.val]

    rotate_pos = pos%n
    rotate_pos = n-rotate_pos if rotate_pos > 0 else 0
    current = head
    n = 0

    while current:
        n += 1
        if n == rotate_pos:
            temp = current.next
            current.next = None
            break
        current = current.next
    if rotate_pos != 0:
        last.next = head
        head = temp

    current = head
    while current:
        ans.append(current.val)
        current = current.next

    return ans

if __name__ == "__main__":
    ll = LinkList([(lambda x: int(x))(x) for x in input().split()])
    pos = int(input())
    print(solve(ll.head, pos))
