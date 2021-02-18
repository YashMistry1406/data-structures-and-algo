# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.result=0
        self.max_depth=0
        def inorder(root,h):
            if root ==None:
                return 0
            if h >self.max_depth:
                self.result=root.val
                self.max_depth=h
            elif h == self.max_depth:
                self.result+=root.val
            inorder(root.left,h+1 )
            inorder(root.right,h+1)
        inorder(root,1)
        return self.result
