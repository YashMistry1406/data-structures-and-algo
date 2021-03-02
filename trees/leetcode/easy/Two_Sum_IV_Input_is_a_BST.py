# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def findTarget(self, root: TreeNode, k: int) -> bool:
#         S = {root.val}
#         stack = [root.left, root.right]
#         while stack:
#             node = stack.pop()
#             if node:
#                 if k - node.val in S:
#                     return True
#                 S.add(node.val)
#                 stack.extend([node.left, node.right])
#         return False
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        output = []
        self.inorder(root,output)
        l,r = 0 ,len(output) - 1
        while l < r:
            Sum = output[l] + output[r]
            if Sum == k:
                return True
            else:
                if Sum < k:
                    l += 1
                else:
                    r -= 1
        return False
    def inorder(self,root,output):
        if root == None:
            return
        else:
            self.inorder(root.left,output)
            output.append(root.val)
            self.inorder(root.right,output)
