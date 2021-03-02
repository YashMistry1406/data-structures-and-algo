# Given two binary trees original and cloned and given a reference to a node target in the original tree.
#The cloned tree is a copy of the original tree.
#Return a reference to the same node in the cloned tree.
#Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
#Follow up: Solve the problem if repeated values on the tree are allowed.
# Definition for a binary tree node.
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(o: TreeNode, c: TreeNode):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    self.ans = c
                inorder(o.right, c.right)
                
        inorder(original, cloned)
        return self.ans 
