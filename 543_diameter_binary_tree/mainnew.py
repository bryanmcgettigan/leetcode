# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    


def diameterOfBinaryTree(root):
    return diameterOfBinaryTreeHelper(root)

def diameterOfBinaryTreeHelper(root):
    maxi=0
    def depth(root):
        print("MAXIMUM: " + str(maxi))
        leftDepth=0
        rightDepth=0
        if root.left == None and root.right == None:
            return 1
        if root.left:
           leftDepth= depth(root.left) + 1
        
        if root.right:
           rightDepth= depth(root.right) + 1
        
        maxi = max(maxi,leftDepth+rightDepth)

        return max(leftDepth,rightDepth)
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    depth(root)
    return maxi








# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)

root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print(diameterOfBinaryTree(root))