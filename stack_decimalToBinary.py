from stack_intro import Stack

stack = Stack()

def dec_to_Binary(inputVal):
    
    iter = inputVal
    while iter is not 0:
        stack.push(iter%2)
        iter = iter//2
    
    retVal = ""
    while not stack.isEmpty():
        retVal = retVal + str(stack.pop())

    return retVal


num = 242
print(dec_to_Binary(num))





