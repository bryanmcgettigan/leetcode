def binarySearch(nums,target):
    end = len(nums)-1
    start=0
    mid=0
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            start=mid+1
        else:
            end=mid-1
    return -1




nums=[2,3,4,10,40]
print(binarySearch(nums,10))