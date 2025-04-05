class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        lSum=0

        def helper_dfs(root):
            nonlocal lSum
            if root:
                if root.left:
                    lSum=lSum+root.left.val
                helper_dfs(root.left)
                helper_dfs(root.right)
        
        helper_dfs(root)

        return lSum






def build_tree():
    root = TreeNode(5)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.left.left = TreeNode(7)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(1)
    return root

root = build_tree()
solution = Solution()

print(solution.sumOfLeftLeaves(root))