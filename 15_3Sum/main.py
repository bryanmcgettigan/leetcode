class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rList = []
        s = set()

        sNums = sorted(nums)
        for index in range(0,len(sNums)-2):
            cNum=sNums[index]
            left=index+1
            right=len(sNums)-1
            while left<right:
                if cNum+sNums[left]+sNums[right]==0:
                    s.add((cNum,sNums[left],sNums[right]))
                    left=left+1
                    right=right-1
                elif cNum+sNums[left]+sNums[right]<0:
                    left=left+1
                else:
                    right=right-1
        rList=list(s)
        return rList

        

solution = Solution()

nums=[-2,0,1,1,2]
print(solution.threeSum(nums))