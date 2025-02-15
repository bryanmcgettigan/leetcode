class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def minDepth(self, root):
        lDepth =0
        rDepth=0

        def depth(root):
            if root:
                if not root.left and not root.right:
                    return 1
                if root:
                    if root.left and not root.right:
                        return depth(root.left)+1
                    elif root.right and not root.left:
                        return depth(root.right)+1
                    return min(depth(root.left),depth(root.right))+1
            return 0
        return depth(root)

# Given input list
arr = [2, None, 3, None, 4, None, 5, None, 6]
root = insert_right_skewed([val for val in arr if val is not None])  # Filtering None values

solution=Solution()

print(solution.minDepth(root))