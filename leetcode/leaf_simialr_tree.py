# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.v1=[]
        self.v2=[]
        
        
        def order(root,v):
            if root ==None:
                return 
            
            if not root.left and not root.right:
                v.append(root.val)
            
            order(root.left,v)
            order(root.right,v)
            
        order(root1,self.v1)
        order(root2,self.v2)
        
        return self.v1==self.v2
    
                
                
