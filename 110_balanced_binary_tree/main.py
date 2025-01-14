class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



def isBalanced(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    def depth(root):
        if root is None:
            return 0
        else:
            l_depth=depth(root.left)
            r_depth=depth(root.right)
        return max(l_depth,r_depth)+1
    
    if root is None:
        return True

    left_depth = depth(root.left)
    right_depth = depth(root.right)

    if (not isBalanced(root.left) or not isBalanced(root.right)):
        return False
    if(abs(left_depth-right_depth)>1):
        return False       

    return True
            
t6=TreeNode(val=6) 
t5=TreeNode(val=5,right=t6)
t4 = TreeNode(val=4,left=t6)
t2 = TreeNode(val=2,left=t4)
t3 = TreeNode(val=3,right=t5)
t1 = TreeNode(val=1,left=t3,right=t2)

print(isBalanced(t1))