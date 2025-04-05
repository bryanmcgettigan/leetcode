
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root:
            if targetSum-root.val==0:
                if not root.left and not root.right:
                    return True
            return self.hasPathSum(root.left,targetSum-root.val)or self.hasPathSum(root.right,targetSum-root.val)
        return False
            







def build_tree():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)
    return root
root = build_tree()
targetSum=28
solution = Solution()



print(solution.hasPathSum(root,targetSum))