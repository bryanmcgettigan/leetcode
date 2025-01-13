#Must be atlease O(log n) 
#Binary search
def search( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start =0
    end = len(nums)-1

    while start <=end:
        mid = start + (end-start) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(search(nums,target))
