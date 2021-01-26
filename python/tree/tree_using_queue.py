
# creation of a linked list tyoe of connection beteween the 
# nodes where in each node is divided in 3 parts 
# left->pointing to the left node and left part of the tree or the samller value 
# center-> It has the data 
# right ->pointing to the left node and left part of the tree or the samller value 
class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None








#creating a node and inserting the value for 
#newly created node 
#greater value is pushed at right 
#while the smaller value than the previous node ios pushed at left side 
#it is recursive function and goes until the root parameter becomes zero 
#after that it creates a new node 
#which then followed by the link formation 
#and at the end of the recursive 
#function the last leaf is connected to the main root of the tree 

def Insert(root,data):
    if(root==None):
        root=Node(data)
    elif(root.data<=data):
        root.left=Insert(root.left,data)
    elif(root.data>data):
        root.right=Insert(root.right,data)
    return root









#finding the minimum in the tree
def findMin(root):
    if(root ==None):
        print("not found")
        return -1
    temp=root.data
    left_min=findMin(root.left)
    right_min=findMin(root.right)
    if left_min<temp:
        temp=left_min
    else:
        temp=right_min
    return temp


#insert maxfor finding a max form the tree 

#def findMin(root):
#    if(root ==None):
#        print("not found")
#        return -1
#    temp=root.data
#    left_min=findMin(root.left)
#    right_min=findMin(root.right)
#    if left_min<temp:
#        temp=left_min
#    else:
#        temp=right_min
#    return temp






#Height of node – The height of a node is the number of edges on the longest downward path 
#between that node and a leaf.
#depth =height-1
#
def FindHeight(root):
    if(root ==None):
        return -1
    return max(FindHeight(root.right),FindHeight(root.left))+1




def level_order(root):
    if(root == None):
        return;
    queue=[]
    queue.append(root)
    while(len(queue)>0):
        print(queue[0].data)
        node=queue.pop()
        if node.right is not None:
            queue.append(node.right)
        if node.left is not None:
            queue.append(node.left)






















if __name__=='__main__':

    tree=Node(1)
    tree=Insert(tree,2)
    tree=Insert(tree,3)

#tree=BinaryTree(1)
#tree.root.left = Node(2)
#tree.root.right = Node(3)
#tree.root.left.left = Node(4)
#tree.root.left.right = Node(5)
#tree.root.right.left = Node(6)
#tree.root.right.right = Node(7)
