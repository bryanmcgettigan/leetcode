class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxValue=0
        for index in range(0,len(nums)-2):
            cNum = nums[index]
            for secondIndex in range(1,len(nums)-1):
                secondNum=nums[secondIndex]
                for thirdIndex in range(2,len(nums)):
                    thirdNum=nums[thirdIndex]
                    if ((cNum-secondNum)*thirdNum)>maxValue and index<secondIndex and secondIndex<thirdIndex:
                        maxValue=(cNum-secondNum)*thirdNum
        return maxValue


solution = Solution()

nums=[12,6,1,2,7]
print(solution.maximumTripletValue(nums))