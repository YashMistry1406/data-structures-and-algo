#class Node:
#    def __init__(self,data):
#        self.data=data
#        self.next=None
#class Linkedlist:
#
#    def __init__(self):
#        self.head=None
#
#
#    def push(self, new_data):
#        new_node=Node(new_data)
#        new_node.next=self.head
#        self.head=new_node
#    #checking for any loops 
#    def detectLoop(self):
#        temp=self.head
#        s=set()
#        while(temp):
#            if (temp in s):
#                return True
#            else:
#                s.add(temp)
#            temp=temp.next
#        return False
# 
# 
## Driver program for testing
#llist = Linkedlist()
#llist.push(20)
#llist.push(4)
#llist.push(15)
#llist.push(10)
# 
## Create a loop for testing
#llist.head.next.next.next.next = llist.head
# 
#if(llist.detectLoop()):
#    print("Loop found")
#else:
#    print("No Loop ")
