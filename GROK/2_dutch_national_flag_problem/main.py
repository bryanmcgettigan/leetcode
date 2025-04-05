class Solution:
  def sort(self, arr):
    # TODO: Write your code here
    n=len(arr)

    low = 0 
    mid = 0
    high = n-1
    while mid<=high:
        cNum=arr[mid]

        if cNum==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low=low+1
            mid=mid+1
        if cNum==1:
           mid=mid+1
        if cNum==2:
           arr[high],arr[mid]=arr[mid],arr[high]
           
           high=high-1
      
      
    return arr


solution = Solution()

arr=[2,2,0,1,2,0]
print(solution.sort(arr))