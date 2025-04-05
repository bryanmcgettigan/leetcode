class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        

        n = set()
        rList=[]
        sNums = sorted(nums)
        for index in range(0,len(sNums)-3):
            for secondIndex in range(index+1,len(sNums)-2):
                left = secondIndex+1
                right=len(sNums)-1
               
                while left<right:
                    cSum = sNums[index]+sNums[secondIndex]+sNums[left]+sNums[right]
                    if cSum==target:
                        n.add((sNums[index],sNums[secondIndex],sNums[left],sNums[right]))
                        left=left+1
                        right=right-1
                    elif cSum<target:
                        left=left+1
                    else:
                        right=right-1
        print(sNums)
        rList = list(n)

        return rList
                    


        


solution=Solution()


nums=[1,0,-1,0,-2,2]


print(solution.fourSum(nums,0))