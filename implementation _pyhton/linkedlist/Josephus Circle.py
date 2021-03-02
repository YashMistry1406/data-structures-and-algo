class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

def lastlife(m,n):
    head=Node(1)
    prev=head 
    
    for i in range (2,n+1):
        prev.next=Node(i)
        prev=prev.next
    prev.next=head



    ptr1=head
    ptr2=head

    while (ptr1.next != ptr1):
        # Find m-th node
        count = 1
        while (count != m):
            ptr2 = ptr1
            ptr1 = ptr1.next
            count += 1
 
        # /* Remove the m-th node */
        ptr2.next = ptr1.next
        # free(ptr1)
        ptr1 = ptr2.next
 
    print("Last person left standing (Josephus Position) is ", ptr1.data)
 
# /* Driver program to test above functions */
if __name__ == '__main__':
#    n = 14
#    m = 2
    n,m=map(int,input().split())
    lastlife(m, n)















