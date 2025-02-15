#Todo
class Solution:
    def search(self, nums, target):

        start = 0
        end = len(nums)-1
       
        while start <end:

            mid = start + (end-start)//2
            num = nums[mid]
            if num==target:
                return mid 
            elif num<target:
                start=mid+1
            else:
                end = mid-1
        return -1           



solution = Solution()

nums=[1,2,3,4,5,6,7,8,9]

print(solution.search(nums,7))