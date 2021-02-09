# Definition for a binary tree node.
#Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
#
#As a reminder, a binary search tree is a tree that satisfies these constraints:
#
#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root):
        self.total = 0
        def dfs(root):
            if root==None:
                return 0
            dfs(root.right)
            self.total +=  root.val
            root.val= self.total
            dfs(root.left)
        dfs(root)
        return root
