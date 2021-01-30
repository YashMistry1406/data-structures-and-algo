#You are given the root of a binary tree where each node has a value 0 or 1.
#Each root-to-leaf path represents a binary number starting with the most significant bit.
#For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
#
#For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
#
#Input: root = [1,0,1,0,1,0,1]
#Output: 22
#Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.result=0
        def preorder(root,curr_sum):
            if not root: return 
            if not root.left and not root.right: 
                self.result+=(curr_sum<<1)+root.val
                print(self.result)
                return
            preorder(root.left,(curr_sum<<1)+root.val) 
            preorder(root.right,(curr_sum<<1)+root.val)

        preorder(root,0)
        return self.result
