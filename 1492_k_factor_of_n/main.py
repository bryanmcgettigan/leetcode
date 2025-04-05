class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """ 
        kList = []
        for num in range(1,(n//2)+1):
            if n%num==0:
                kList.append(num)
                if k==len(kList):
                    return kList[k-1]
        kList.append(n)
        if k>len(kList):
            return -1
        else:
            return kList[k-1]

        

solution = Solution()

n=12
k=3

print(solution.kthFactor(n,k))