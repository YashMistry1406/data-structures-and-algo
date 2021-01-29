# Definition for a binary tree node.
#Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
#Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
#Output: 32
#we recusively go through the all the node and when ever a node whose value in more than the low 
#and less than the high we add it to ans 
#when ever a node whose value is more than the low we iterate through the left half










#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.sum_ = 0
        def recursion(root, low,high):
            if not root:
                return 0
            if root.val<=high and root.val>=low:
                self.sum_ += root.val
            if root.val<low:
                recursion(root.right,low,high)
            elif root.val>high:
                recursion(root.left,low,high)
            else:
                recursion(root.left, low,high)
                recursion(root.right,low,high)
        recursion(root,low,high)
        return self.sum_
