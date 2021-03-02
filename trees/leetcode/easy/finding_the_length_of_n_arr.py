class Solution1(object):
    def maxDepth(self, root):
        if not root: return 0 #base case 1
        if not root.children: return 1 #base case 2
        heights = [] #hold all the heights of root's children 
        for node in root.children:
            heights.append(self.maxDepth(node))
        return max(heights) + 1


#Simplify solution 1
class Solution2(object):
    def maxDepth(self, root):
        if not root: return 0
        if not root.children: return 1
        height = [self.maxDepth(node) for node in root.children]
        return max(height) + 1


#improve it one more step
class Solution3(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        if not root.children: return 1
        return max(self.maxDepth(node) for node in root.children) + 1   


#Compare the heights in a loop
class Solution4(object):
    def maxDepth(self, root):
        if not root: return 0
        height = 0
        for node in root.children:
            height = max(self.maxDepth(node), height)
        return height + 1
