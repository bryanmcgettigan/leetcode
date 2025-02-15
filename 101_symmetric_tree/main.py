class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(roota,rootb):
            if roota is None and rootb is None:
                return True
            if roota is None or rootb is None:
                return False
            
            if roota.val==rootb.val:
                return dfs(roota.left,rootb.right) and dfs(roota.right,rootb.left)
            print(str(roota.val) + " " + str(rootb.val))
            return False
        if root:
            return dfs(root.left,root.right)
        return False
    
def insert_level_order(arr, root, i, n):
    if i < n and arr[i] is not None:
        temp = TreeNode(arr[i])
        root = temp
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root

# Given input list
arr = [1, 2, 2, 3, 4, 4, 3]
n = len(arr)
root = insert_level_order(arr, None, 0, n)

solution=Solution()
print(solution.isSymmetric(root))