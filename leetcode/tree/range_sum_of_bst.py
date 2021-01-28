# Definition for a binary tree node.
#Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
#Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
#Output: 32









class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans
