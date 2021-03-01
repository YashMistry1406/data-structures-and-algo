# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.count=0
        def solve(root):
            if root==None:
                return 0
            self.count+=1
            solve(root.left)
            solve(root.right)

            return self.count
        return self.count//2


