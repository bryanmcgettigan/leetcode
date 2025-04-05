class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest=100000000
        sNums=sorted(nums)
        print(sNums)
        for index in range(0,len(sNums)-2):
            left = index+1
            right=len(sNums)-1
            cNum=sNums[index]
            while left<right:
                
                if abs(target-(sNums[left]+sNums[right]+cNum)) < abs(target-closest):

                    closest=abs(sNums[left]+sNums[right]+cNum)


                elif (sNums[left]+sNums[right]+cNum)<target:
                    left=left+1
                else:
                    right=right-1
        return closest
        

solution = Solution()

nums=[-1,2,1,-4]

print(solution.threeSumClosest(nums,1))

print(abs(-1-1))