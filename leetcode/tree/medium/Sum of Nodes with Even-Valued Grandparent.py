#1315. Sum of Nodes with Even-Valued Grandparent
#Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)
#
#If there are no nodes with an even-valued grandparent, return 0.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack= [root]
        s = 0
        while stack:
            curr = stack.pop()
            if curr:
                stack+=[curr.right, curr.left]
                if curr.val%2==0:
                    if curr.left:
                        if curr.left.left:
                            s+=curr.left.left.val
                        if curr.left.right:
                            s+=curr.left.right.val
                    if curr.right:
                        if curr.right.left:
                            s+=curr.right.left.val
                        if curr.right.right:
                            s+=curr.right.right.val
        return s
