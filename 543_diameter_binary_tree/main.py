# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
    
     def depth(self):
        leftDepth=0
        rightDepth=0
        if self.left == None and self.right == None:
            return 1
        if self.left:
           leftDepth= self.left.depth() + 1
        
        if self.right:
           rightDepth= self.right.depth() + 1

        return max(leftDepth,rightDepth)

hmap={}

def diameterOfBinaryTree(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    lDepth = 0
    rDepth = 0
    if root.left:
        lDepth = root.left.depth()
    if root.right:
        rDepth = root.right.depth()
    mpath = lDepth+rDepth
    hmap[root] = mpath
    
    if root.left == None and root.right == None:
        return 0
    if root.left:
        diameterOfBinaryTree(root.left)
    
    if root.right:
        diameterOfBinaryTree(root.right)
    print(hmap)
    return max(hmap.values())








# Construct a binary tree
root = TreeNode(1)
root.left = TreeNode(2)

root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print(diameterOfBinaryTree(root))