class Stack:
    def __init__(self):
        self.itim = []

    def is_empty(self):
        return len(self.itim) == 0

    def push(self, son):
        return self.itim.insert(0, son)

    def pop(self):
        if not self.is_empty():
            return self.itim.pop()
        else:
            print("List bosh ")

    def print_stack(self):
        if not self.is_empty():
            return self.itim

    def size(self):
        return len(self.itim)


stack = Stack()
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(6)
print(stack.print_stack())
# print(stack.is_empty())
# print(stack.pop())
# print(stack.size())