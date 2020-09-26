# !/usr/bin/python3

class MInStack:
    def __init__():
        stack = []
        mi = float("-inf")

    def push(self, x: int) -> None:
        self.stack.apeend(x)
        self.mi = min(mi, x)

    def pop(self) -> None:
        try:
            self.stac.pop()
            mi = min(self.stack)
        except:
            print("Create a stack")

    def top(self) -> int:
        try:
            return self.stack[-1]
        except:
            print("Create a stack")

    def get_min(self, ):
        try:
            return self.mi
        except:
            print("Create a stack")


if __name__ == "__main__":
    obj = MinStack()
