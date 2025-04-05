#TODO

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        sum =[0]
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                if root.left and root.right:
                    sum[0] = sum[0]+abs(root.left.val-root.right.val)
                if root.left and not root.right:
                    sum[0] = sum[0] + root.left.val
                if root.right and not root.left:
                    sum[0] = sum[0] + root.right.val
        dfs(root)
        return sum[0]

        

def build_tree():
    root = TreeNode(5)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(4)
    return root

root = build_tree()
solution = Solution()

print(solution.findTilt(root))