#iterative traversal of a n-ary tree traversal
#first we append the root in the stack and then we loop through
#the stack popping the last node in a temp variable
#and if the root is not null we pass throughits children
#using the extended function refer net for extend function 
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         if root==None:
#             return []
#         res=[]
#         stack=[]
#         stack.append(root)
#         while stack:
#             temp=stack.pop()
#             res.append(temp.val)
#             temp_node=temp.children
#             print(temp.children)
#             stack+=(temp_node[::-1])
#         return res 

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # corner case
        #
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.extend(root.children[::-1]) 
        return res

