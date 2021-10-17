# class Stack():
#     def __init__(self):
#         self.items = []

#     def push(self,ele):
#         self.items.append(ele)

#     def pop(self):
#         return self.items.pop()

#     def isEmpty(self):
#         return self.items == []

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]

#     def getStack(self):
#         return self.items

from stack_intro import Stack

def is_match(p1,p2):
    if p1 == "(" and p2 == ")":
        return True
    if p1 == "{" and p2 == "}":
        return True
    if p1 == "[" and p2 == "]":
        return True
    else:
        return False

def isParenBalanced(paren_string):
    s = Stack()
    isBalanced = True
    i = 0

    while i < len(paren_string) and isBalanced:
        paren = paren_string[i]
        if paren in "({[":   #i.e if it is a opening bracket
            s.push(paren)
        else:                #i.e if it is a closing bracket
            if s.isEmpty():
                isBalanced = False
                break
            else:
                top = s.pop()
                if not is_match(top,paren):
                    isBalanced = False
                    break
        
        i = i + 1

    if s.isEmpty() and isBalanced:
        return True
    else:
        return False

print(isParenBalanced('(({]}}'))

