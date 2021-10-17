class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next
        
    def prepend(self,data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insertAfterNode(self,prev_node,data):
        if(prev_node is None):
            print("Sorry, the previous node does not exist!")
            return
        
        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node


    def deleteNode(self,key):
        cur_node = self.head
        if cur_node.data is key:
            self.head = cur_node.next
            del(cur_node)
            return

        prev_node = None
        while cur_node and cur_node.data is not key:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        else:
            prev_node.next = cur_node.next
            del(cur_node)
    
    def deleteByPos(self,pos):
        cur_node = self.head

        if pos == 1 and cur_node:
            self.head = cur_node.next
            del(cur_node)
            return

        prev_node = None
        i = 1
        while cur_node and i != pos:
            prev_node = cur_node
            cur_node = cur_node.next
            i = i + 1
        
        if cur_node is None:
            return
        
        prev_node.next = cur_node.next
        del(cur_node)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        


    def getLength(self):
        l = 0
        cur_node = self.head
        while cur_node:
            l = l + 1
            cur_node = cur_node.next
        return l
        

    def getLengthRecursive(self,node):
        if node is None:
            return 0
        else:
            return 1  +  self.getLengthRecursive(node.next)



sllist = LinkedList()

sllist.append('W')
sllist.append('X')
sllist.append('Y')
sllist.append('A')
sllist.print_list()
sllist.prepend('V')
print('post prepending V')
sllist.print_list()
prevnode = sllist.head.next.next #i.e X
sllist.insertAfterNode(prevnode,'K')
print('post Inserting after X')
sllist.print_list()
sllist.deleteNode('X')
print('Post deleting X ')
sllist.print_list()
# print(id(sllist.head.data))
sllist.deleteByPos(0)
print('Post deleting element at 3rd posisiton(considering 0th position for first element')
sllist.print_list()
print('Length of the current Linked List: ' + str(sllist.getLength()))
print('Length of the current Linked List (Recursively): ' + str(sllist.getLengthRecursive(sllist.head)))

