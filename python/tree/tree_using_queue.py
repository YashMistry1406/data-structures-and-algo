class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None



def Insert(root,data):
    if(root==None):
        root=Node(data)
    elif(root.data<=data):
        root.left=Insert(root.left,data)
    elif(root.data>data):
        root.right=Insert(root.right,data)
    return root
#tree=BinaryTree(1)
#tree.root.left = Node(2)
#tree.root.right = Node(3)
#tree.root.left.left = Node(4)
#tree.root.left.right = Node(5)
#tree.root.right.left = Node(6)
#tree.root.right.right = Node(7)
if __name__=='__main__':

    tree=Node(1)
    tree=Insert(tree,2)
    tree=Insert(tree,3)


