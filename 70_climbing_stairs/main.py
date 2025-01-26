
def helper(cache,n):

    if n<2:
        cache[n]= 1
    if n not in cache:
        cache[n]= helper(cache,n-1) + helper(cache,n-2)

    return cache[n]

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    cache={}
    return helper(cache,n)

    
print(climbStairs(45))
