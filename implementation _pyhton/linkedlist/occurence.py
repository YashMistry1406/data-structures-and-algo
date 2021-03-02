class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:

    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def count(self,search):
        current=self.head
        count=0
        while(current is not None):
            if  current.data==search:
                count+=1
            current=current.next
        return count
llist = LinkedList() 
llist.push(1) 
llist.push(3) 
llist.push(1) 
llist.push(2) 
llist.push(1) 
  
# Check for the count function 
print ("count of 1 is % d" %(llist.count(1)) )
