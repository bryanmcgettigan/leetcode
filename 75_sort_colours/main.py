class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums[0] !=0:
            left=1
            while nums[left] !=0 and left<len(nums):
                left=left+1
            nums[0],nums[left]=nums[left],nums[0]
             
        for index in range(0,len(nums)-1):
            right=index+1
            while nums[right]>nums[index]:
                nums[index]
            



solution= Solution()

nums=[2,0,2,1,1,0]
print(solution.sortColors(nums))