class Solution(object):
    def backspaceCompare(self, S, T):
        def back(res, c):
            if c != '#': res.append(c)
            elif res: res.pop()
            return res
        return reduce(back, S, []) == reduce(back, T, [])
        
            
            

        
s="#a#c"
t="#a#c"
solution = Solution()

result = solution.backspaceCompare(s,t)

print(result)