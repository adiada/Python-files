from stack_intro import Stack
stack = Stack()

def rev_string(inpString):
    for i in range(len(inpString)):
        stack.push(inpString[i])

    revStr=""
    while not stack.isEmpty():
        revStr = revStr + stack.pop()

    return revStr

inp = "Hello! Welcome to nohtyP"

print(rev_string(inp))

