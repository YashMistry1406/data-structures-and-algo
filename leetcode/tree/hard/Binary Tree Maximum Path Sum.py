# question-https://leetcode.com/problems/binary-tree-maximum-path-sum/
# solution--which i referred to
#             https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram






class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
            max_path = float("-inf") 
            def get_max_gain(node):
                nonlocal max_path 
                if node is None:
                    return 0

                gain_on_left = max(get_max_gain(node.left), 0)
                print(gain_on_left)
                gain_on_right = max(get_max_gain(node.right), 0)  
                

                current_max_path = node.val + gain_on_left + gain_on_right 
                max_path = max(max_path, current_max_path) 
                return node.val + max(gain_on_left, gain_on_right) 
            get_max_gain(root) 
            return max_path		