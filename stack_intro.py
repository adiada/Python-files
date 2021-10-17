class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def get_stack(self):
        return self.items


# myStack = Stack()
# myStack.push(3)
# myStack.push(2)
# myStack.push(5)
# myStack.push(8)
# myStack.push(10)
# print(myStack.get_stack())
# print(myStack.pop())
# print(myStack.peek())
# print(myStack.isEmpty())