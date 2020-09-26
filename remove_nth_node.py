# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/remove-nth-node-from-list-end/
Remove nth node.
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
        current = current.next
    from_start = n-pos+1
    current = head
    prev = None
    n = 0
    while current:
        n += 1
        if n == from_start:
            if prev == None:
                head = current.next
            else:
                prev.next = current.next
            break
        prev = current
        current = current.next

    current = head
    while current:
        ans.append(current.val)
        current = current.next
    return ans

if __name__ == "__main__":
    ll = LinkList([(lambda x: int(x))(x) for x in input().split()])
    pos = int(input())
    print(solve(ll.head, pos))
