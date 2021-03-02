#infinite loop 
#code for deleting a node and adding a ode in cicular linkedlist 
#check net not working





class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
class Delcircular:
    def __init__(self):
        self.last=None

# This function is only for empty list
    def addToEmpty(self, data):
        if (self.last != None):
            return self.last
 
        # Creating the newnode temp
        temp = Node(data)
        self.last = temp
 
        # Creating the link
        self.last.next = self.last
        return self.last
 

    def addEnd(self,data):
        new_node=Node(data)
        temp=self.last.next
        new_node=self.last.next 
        self.last.next=new_node
        self.last=new_node
    def addBegin(self,data):
        temp=Node(data)
        temp.next=self.last.next
        self.last=temp
    def printList(self): 
        temp = self.last
        while (temp): 
            print (temp.data,) 
            temp = temp.next
 
        temp = self.last.next
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
            if temp == self.last.next:
                break
if __name__ == '__main__':
 
    llist =Delcircular()
 
    last = llist.addToEmpty(6)
    last = llist.addBegin(4)
    last = llist.addBegin(2)
    last = llist.addEnd(8)
    last = llist.addEnd(12)
    #last = llist.addAfter(10,8)
 
    llist.printList()
