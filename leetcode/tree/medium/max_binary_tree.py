# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums)==1:
            return TreeNode(nums[0])
        temp=max(nums)
        index=nums.index(temp)
        root=TreeNode(temp)
        root.left=self.constructMaximumBinaryTree(nums[0:index])
        root.right=self.constructMaximumBinaryTree(nums[index+1:])
        return root
"""
the logic is that
we travel through the list and pass list and store the max of that current list in the temp variable 
now we get the index of that temp variable
now on getting the variable index we pass the list to the constructMaximumBinaryTree with the index updated 
recusively calling the function and end it by returning the root
"""
