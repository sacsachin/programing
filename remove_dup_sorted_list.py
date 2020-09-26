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

def solve(head):
    current = head
    n = 0
    ans = []
    while current:
        n += 1
        current = current.next
    if n == 1:
        return [head.val]
    prev = head
    current = head.next
    while current:
        if prev.val == current.val:
            prev.next = current.next
            current = current.next
        else:
            prev = current
            current = current.next
    current = head
    while current:
        ans.append(current.val)
        current = current.next

    return ans

if __name__ == "__main__":
    ll = LinkList([(lambda x: int(x))(x) for x in input().split()])
    print(solve(ll.head))
