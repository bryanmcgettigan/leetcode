class Solution:
  def makeSquares(self, arr):
    n = len(arr)

    if n==1:
        return [arr[0]*arr[0]]
    squares = []

    lPoint=0
    rPoint=1

    while arr[rPoint]<0 and rPoint<len(arr)-1:
        rPoint = rPoint+1
    lPoint=rPoint-1


    while lPoint>=0 and rPoint<len(arr):
        if (arr[rPoint]*arr[rPoint])>(arr[lPoint]*arr[lPoint]):
            squares.append(arr[lPoint]*arr[lPoint])
            lPoint=lPoint-1
        else:
            squares.append(arr[rPoint]*arr[rPoint])
            rPoint=rPoint+1
    
    while lPoint>=0:
        squares.append(arr[lPoint]*arr[lPoint])
        lPoint=lPoint-1

    while rPoint<len(arr):
            squares.append(arr[rPoint]*arr[rPoint])
            rPoint=rPoint+1


    return squares


solution = Solution()
arr=[-3, -2, -1]
print(solution.makeSquares(arr))