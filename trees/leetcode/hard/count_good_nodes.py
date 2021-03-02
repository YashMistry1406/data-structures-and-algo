#Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
#
#Return the number of good nodes in the binary tree.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # use a parameter to store current max node.val in the path
		# answer
        self.count = 0
        
        def recur(root, maxi):
            if not root:
                return
            
            if root.val >= maxi:
                self.count += 1
                maxi = root.val
            
            recur(root.left, maxi)
            recur(root.right, maxi)
        
        recur(root, float('-inf'))
        
        return self.count

