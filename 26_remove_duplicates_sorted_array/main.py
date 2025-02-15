class Solution(object):
    def removeDuplicates(self, nums):
        index =0 
        hmap={}
        while index<len(nums):
            
            hmap[nums[index]] = hmap.get(nums[index],0)+1
            
            if hmap[nums[index]]>1:
                nums.pop(index)
                index = index-1
            index=index+1
        return len(nums)

        
solution = Solution()
nums=[1,1,1,2]
print(solution.removeDuplicates(nums))

print(nums)