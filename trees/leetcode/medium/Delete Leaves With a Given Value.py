#Given a binary tree root and an integer target, delete all the leaf nodes with value target.
#
#Note that once you delete a leaf node with value target, if it's parent node becomes a leaf node and has the value target, it should also be deleted 
#(you need to continue doing that until you can't).

#we are only deleting the leaf and if a node to whom the leaf belonged to also has the value of targeted value then 
#it is also deleted or else we leave the node as it is 
#say example [1,2,3] ---> in the following eg 1 is the node and even if the targeted node is 1 we cannot delete it 






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root.left:
            root.left=self.removeLeafNodes(root.left,target)
        if root.right:
            root.right=self.removeLeafNodes(root.right,target)
        if root.left==None and root.right==None and root.val ==target:
            return None
        return root
        
        
