class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def Insert(root,data):
    if(root== None):
        root=Node(root)
    if(root.data <=data):
        root.left=Insert(root.left,data)
    elif(root.right >data):
        root.right=Insert(root.right,data)
    return root

def BSTUtil(root,minValue,maxValue):
    if(root==None):
        return True
    if(root.data>minValue and root.data>maxValue and
       BSTUtil(root.left,minValue,root.data) and
       BSTUtil(root.right,root.data,maxValue)):
        return True
    else:
        return False




if __name__=='__main__':
    tree=Node(1)
    tree=Insert(tree,2)
    tree=Insert(tree,3)


