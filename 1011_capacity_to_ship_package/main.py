class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def feasible(capacity):
            days_spent=0
            index=0
            cTotalWeight=0
            while index<=len(weights)-1:
                if weights[index]>capacity:
                    return False
                if (cTotalWeight+weights[index])<=capacity:
                    cTotalWeight=cTotalWeight+weights[index]
                    index=index+1
                else:
                    days_spent = days_spent+1
                    cTotalWeight=0
            days_spent=days_spent+1           
            return days_spent<=days
        
        end = sum(weights)
        start = max(weights)
        mid=0

        while start<end:
            mid=(start+end)//2
            if feasible(mid):
                end = mid
            else:
                start=mid+1
        return start


solution = Solution()

weights=[3,2,2,4,1,4]
days=3



#print(feasible(5))

print(solution.shipWithinDays(weights,days))