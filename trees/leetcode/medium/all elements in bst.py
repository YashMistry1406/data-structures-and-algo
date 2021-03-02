# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        
        self.stack=[]
        
        def inorder(root):
            if root==None:
                return 
            inorder(root.left)
            self.stack.append(root.val)
            inorder(root.right)
        stack2=[]
        r1=inorder(root1)
        # stack2.append(self.stack)
        r2=inorder(root2)
        # stack2.append(self.stack)
        
        return sorted(self.stack)

