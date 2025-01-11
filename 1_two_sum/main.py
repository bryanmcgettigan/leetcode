def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indextwo=0
    for index,num in enumerate(nums):
        indextwo=index+1
        for numtwo in nums[index+1:]:
            if((numtwo+num)==target and (indextwo != index)):
                return [index,indextwo] 
            indextwo = indextwo+1
        
   
nums=[3,2,95,4,-3]

print(twoSum(nums,92))