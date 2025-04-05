# Definition for a binary tree node.
class TreeNode(object):    
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class Solution(object):
    def maxDepth(self, root):
        
        lDepth=0
        rDepth=0
        def depth_helper(root,depth):
            if root:
                depth=max(depth_helper(root.left,depth),depth_helper(root.right,depth))+1
            return depth
        
        lDepth=depth_helper(root.left,lDepth)
        rDepth=depth_helper(root.right,rDepth)
        return max(lDepth,rDepth)+1


root3 = TreeNode(1)
#root3.right = TreeNode(2)
#root3.right.right = TreeNode(3)
solution = Solution()

print(solution.maxDepth(root3))