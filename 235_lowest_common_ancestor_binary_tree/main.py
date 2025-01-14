class TreeNode(object):
     def __init__(self, val=0,left=None,right=None):
         self.val = val
         self.left = left
         self.right = right


     def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def nodeExists(root,target):
            if root:
                if root.val==target:
                    return True
                return nodeExists(root.left,target) or nodeExists(root.right,target)
            return False

        if not root:
            return None
        
        # If root is either p or q, root is the LCA
        if root == p or root == q:
            return root
        
        # Recur for left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are found in left and right subtrees of root, root is the LCA
        if left and right:
            return root
        return left if left else right

t0 = TreeNode(val=0)
t3 = TreeNode(val=3)
t5 = TreeNode(val=5)
t4 = TreeNode(val=4, left=t3, right=t5)
t7 = TreeNode(val=7)
t9 = TreeNode(val=9)
t2 = TreeNode(val=2, left=t0, right=t4)
t8 = TreeNode(val=8, left=t7, right=t9)
t6 = TreeNode(val=6, left=t2, right=t8)

print(t6.lowestCommonAncestor(root=t6,p=6,q=4))