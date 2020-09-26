# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/add-two-numbers-as-lists/
Add two numbers as list.
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

def solve(first, second):
    n = m = 0

    current = first
    while current:
        n += 1
        current = current.next

    current = second
    while current:
        m += 1
        current = current.next

    if m > n:
        current = first
        first = second
        second = current

    # display(first)
    # display(second)

    temp1 = first
    temp2 = second
    carry = 0
    while temp1 and temp2:
        value = (temp1.val+temp2.val+carry)%10
        carry = (temp1.val+temp2.val+carry)//10
        temp1.val = value
        current = temp1
        temp1 = temp1.next
        temp2 = temp2.next

    # display(first)
    while temp1:
        if carry:
            value = temp1.val
            temp1.val = (value+carry)%10
            carry = (value+carry)//10
        current = temp1
        temp1 = temp1.next
    # print(carry)
    if carry:
        node = Node(carry)
        current.next = node
    # display(first)

    return lis(first)[::]

if __name__ == "__main__":
    ll1 = LinkList(list(map(int, input().split())))
    ll2 = LinkList(list(map(int, input().split())))
    print(solve(ll1.head, ll2.head))
