#TREE
#other are linear that we used till far like list
#we use linkedlist type of implementation 
#there are 3 space to visualize one that holds the data an other tow to hold the address of prev and 
#and next for leaf 
#BINARY TREE :- each tree can have only 2 child 
#at any level we can have max of 
#    2^i nodes 
#where i is the level
#for a tree to be complete tree we need to have allthe nodes to 
#complete 
#balance binary tree :- the differenec between the height of right and
#left subtree for every node is not more than K(mostly 1)
#height of a empty tree is -1
#
#height of a empty tree is -1
#height of a tree with one node is 0
#diff=|h(left)- h(right)|
#BINARY SEARCH TREE
#a binary search treein fro each node value of all the nodes in left 
#subtree is lesser or equal and valur of all the nodes in right subtree
#is greater
#search spaceo is 
#The maximum number of nodes at level ‘l’ of a binary tree is 2l. 
class Node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None 


root=Node(1)
root.left=Node(1)

root.right=Node(2)
# This simply reated a tree with one root and two leaf one onthe right and other on the left 
#now to add to the leaf we need to specify the path


root.left.left=Node(4)

print("complete")













