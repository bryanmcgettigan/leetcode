#TODO
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        hmap = {}
        hmapTrusts={}

        for arr in trust:
            hmap[arr[1]] = hmap.get(arr[1],0)+1
            hmapTrusts[arr[0]]=hmap.get(arr[0],0)+1
        print(hmap)
        print(hmapTrusts)
        print(max(hmap))
        if hmapTrusts.get(max(hmap),0)==0 and max(hmap) ==(n-1):
            return max(hmap)
        return -1
        

solution=Solution()


n=2
trust=[[1,2]]
print(solution.findJudge(n,trust))