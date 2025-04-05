class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        hmap = {}
        stack = []
        stack.append(root)
        while len(stack)>0:
            root=stack.pop()
            if root:
                hmap[root.val] = hmap.get(root.val,0)+1
                stack.append(root.right)
                stack.append(root.left)
        max_val = [keys for keys,values in hmap.items() if values == max(hmap.values())]
        return max_val
        

root = TreeNode(1)
root.left = TreeNode(1)
root.right=TreeNode(2)
root.right.left=TreeNode(2)

solution=Solution()
print(solution.findMode(root))