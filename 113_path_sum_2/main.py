class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        rList = []
        cList=[]
        def helper(root,target):
            if root:
                nonlocal cList
                nonlocal rList
                cList.append(root.val)
                
                if target-root.val==0:
                    if not root.left and not root.right:
                        rList.append(cList)

                        cList=[cList[0]]
                else:
                    if not root.left and not root.right:
                        cList.pop()
                helper(root.left,target-root.val)
                helper(root.right,target-root.val)

        if not root:
            return False
        helper(root,targetSum)

        return rList
        


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
    root.right.right.left = TreeNode(5)
    return root
root = build_tree()
targetSum=20
solution = Solution()

l = solution.pathSum(root,22)

print(l)