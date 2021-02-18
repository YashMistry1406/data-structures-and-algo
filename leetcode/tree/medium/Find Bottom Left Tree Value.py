#Given the root of a binary tree, return the leftmost value in the last row of the tree.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.max_height=0
        self.max_val=0
        def solve(root,l_h):
            if root ==None:
                return 
            l_h+=1
                
            
            if l_h>self.max_height:
                self.max_height=l_h
                self.max_val=root.val
            
            solve(root.left,l_h)
            solve(root.right,l_h)
        
        solve(root,0)
        return self.max_val
        
        
