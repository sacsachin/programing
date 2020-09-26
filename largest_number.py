# !/usr/bin/python3

"""
https://www.interviewbit.com/problems/largest-number/
Largest Number
"""
# from functools import cmp_to_key
def cmp_to_key(my_cmp):
    """convert a cmp function into key function"""
    class K(object):
        def __init__(self, obj, *args):
            print("Obj created with", obj)
            self.obj = obj
        def __lt__(self, other):
            print("Comparing less then", self.obj)
            return my_cmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            print("Comparing greatr then", self.obj)
            return my_func(self, other) > 0
        def __eq__(self, other):
            print("Comparing eqals", self.obj)
            return my_cmp(self.obj, other.obj) == 0
        def __le__(self, other):
            print("Comparing less then eqal", self.obj)
            return my_cmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            print("Comparing greatr then equal", self.obj)
            return my_cmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            print("Comparing not equals", self.obj)
            return my_cmp(self.obj, other.obj) != 0
    return K

def my_cmp(a, b):
    print(a, "  ", b)
    if int(str(a)+str(b)) < int(str(b)+str(a)):
        return -1
    elif int(str(a)+str(b)) > int(str(b)+str(a)):
        return 1
    return 0


if  __name__ == "__main__":
    A = [(lambda x: str(x))(x) for x in input().split(" ")]
    data = {'key': cmp_to_key(my_cmp), 'reverse': True}
    A.sort(**data)
    #A.sort(key=cmp_to_key(my_cmp), reverse=True)
    print(A)
