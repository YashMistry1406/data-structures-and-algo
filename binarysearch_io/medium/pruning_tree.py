# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def allZeros(root):
            if not root:
                return True

            leftZeros = allZeros(root.left)
            rightZeros = allZeros(root.right)
            

            # delete the subtree that is all zeros;)
            if leftZeros:
                root.left = None
            if rightZeros:
                root.right = None

            # returns true if all are zeros...
            return root.val == 0 and leftZeros and rightZeros

        if allZeros(root):
            return None

        return root
