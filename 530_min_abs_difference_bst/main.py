class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        l=[]
        def dfs(root):
            if root:
                dfs(root.left)
                l.append(root.val)
                dfs(root.right)

        dfs(root)
        min=10000000000
        for index in range(0,len(l)-1):
            if abs(l[index]-l[index+1])<min:
                min=abs(l[index]-l[index+1])
        return min


        
t5=TreeNode(val=227)
t4 = TreeNode(val=911)
t2 = TreeNode(val=701,right=t4)
t3 = TreeNode(val=104,right=t5)
t1 = TreeNode(val=236,left=t3,right=t2)



solution = Solution()

print(solution.getMinimumDifference(t1))