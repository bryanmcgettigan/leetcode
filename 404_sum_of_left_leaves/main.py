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
        def dfs(root,isLeft):
            if root is None:
                return 0 
            if not root.left and not root.right:
                if isLeft:
                    return root.val
                return 0
            left_sum=dfs(root.left,True)
            right_sum=dfs(root.right,False)
            return left_sum+right_sum

        return dfs(root,False)




def build_tree():
    root = TreeNode(5)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(4)
    return root

root = build_tree()
solution = Solution()

print(solution.sumOfLeftLeaves(root))