    # n = int(input("Enter a number:"))

    # if n < 0:
    #     print("Enter a positive number")
    # else:
    #     sum = 0

    #     while( n > 0):
    #         sum += n
    #         n -= 1

    #     print("The sum is",sum)


# a=10
# b=12

# print(a^b)


# #code to find the square root of a number using binary search 
# n = 2957

# start = 1
# end = n
# ans = n

# while(start < end):
#     mid = (start + end)//2
#     if(mid*mid > n):
#         end = mid - 1
#     else:
#         ans = mid
#         start = mid + 1

# print(ans)    


# baskets = [1,2,3,4,9]
# n = len(baskets)
# m = 3    #number of balls

# start = 1
# end = baskets[-1] - baskets[0]

#Getting balanced bracket
#expr = "[(){}]"
# expr = "[({)}]"
 
# st = []
 
# def isOpening(char):
#     if (char == '(' or char == '{' or char == '['):
#         return True
#     return False
 
# def characterType(char):
#     if (char == '(' or char == ')'):
#         return 'Round'
#     elif (char == '{' or char == '}'):
#         return 'Curly'
#     else:
#         return 'Square'
 
# for char in expr:
#     if (isOpening(char)):
#         st.append(char)
#     else:
#         if (len(st) == 0):
#             print("Unbalanced!")
#             break
#         else:
#             if (characterType(st[-1]) == characterType(char)):
#                 st.pop()
#             else:
#                 print("Unbalanced!")
#                 break
 
# if (len(st) > 0):
#     print("Unbalanced!")
# else:
#     print("Balanced")



# st = [2,5,1,6,4,9]

# def place(ele,st):
#     if(len(st) == 0):
#         st.append(ele)
#     else:
#         if(st[-1] > ele):
#             st.append(ele)
#         else:




class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


head = None


def insertAtTop(data):
    global head
    nn = Node(data)

    if(head is None):
        head = nn
    else:
        nn.next = head
        head = nn
    
def printLinkedList():
    curr = head
    while (curr is not None):
        print(curr.data)
        curr = curr.next

insertAtTop(10)
insertAtTop(20)
insertAtTop(30)
insertAtTop(40)
insertAtTop(0)


# def printReverse(node):
#     if(node is not None):
#         printReverse(node.next)
        # print(node.data)


#for reversing the Linked list actually(not just printing it reversed)
# def reverseHelper(node):
#     if(node is not None):
#         print("Processing" + str(node.data))
#         if(node.next is None):
#             return node
#         else:
#             curr = node
#             nextNode = node.next
#             last = reverseHelper(node.next)
#             nextNode.next = curr
#             return last

# def reverse(node):
#     global head
#     if(node is not None):
#         last = reverseHelper(node)
#         head.next = None
#         head = last


# printLinkedList()
# reverse(head)
# printLinkedList()

# printReverse(Node)


# st = [2,5,1,6,4,9]

# def place(ele,st):
#     if(len(st) == 0):
#         st.append(ele)
#     else:
#         if(st[-1] > ele):
#             st.append(ele)
#         else:




# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# head.next.next.next.next.next = head.next



# def insertAtTop(data):
#     global head
#     nn = Node(data)

#     if(head is None):
#         head
#     else:
#         nn.next = head
#         head = nn
    
# def printLinkedList():
#     curr = head
#     while (curr is not None):
#         print(curr.data)
#         curr = curr.next

# def detectCycle():
#     slow = head
#     fast = head
#     while(fast is not None and fast.next is not None):
#         slow = slow.next
#         fast = fast.next.next 

#         if(slow is fast):
#             print("Cycle is present")
#             break

# detectCycle()

# printLinkedList()

            

#Implementation of trees

# class Node:
#     def __init__ (self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# root = Node("A")
# root.left = Node("B")
# root.right = Node("C")
# root.left.left = Node("D")
# root.left.right = Node("E")
# root.right.right = Node("F")

# def preOrder(node):
#     if(node is not None):
#         print(node.data)
#         preOrder(node.left)
#         preOrder(node.right)


# def printLevel(node,levelOfParent):
#     if node is not None:
#         myLevel = levelOfParent + 1
#         print("Level of " + str(node.data) + " is " + str(myLevel))
#         printLevel(node.left,myLevel)
#         printLevel(node.right,myLevel)


# def postOrder(node):
#     if(node is not None):
#         postOrder(node.left)
#         postOrder(node.right)
#         print(node.data)

# def inOrder(node):
#     if(node is not None):
#         inOrder(node.left)
#         print(node.data)
#         inOrder(node.right)

# print("Inorder:")
# inOrder(root)
# print("Preorder:")
# preOrder(root)
# print("Postorder:")
# postOrder(root)

# printLevel(root,-1)

 
# DP Problems
# Given N find min no of perfect squares which sum upto N

# def f(n):


#Given coins of different denominations and N, find min number of coins to form N
# Eg:-  coins = [1,2,5] N = 14   Ans = 4 (as 14 = 5 + 5 + 2 + 2)


