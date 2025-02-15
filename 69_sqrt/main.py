class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return -1
        
        start=0
        end=x
        mid=0
        while start<=end:
            mid=(start +end)//2
            square = mid*mid
            if square ==x:
                return mid
            elif square>x:
                end = mid-1
            else:
                start=mid+1
        return end

        
        
solution = Solution()
x=9
print(solution.mySqrt(x))