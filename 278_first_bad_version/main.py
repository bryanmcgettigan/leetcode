def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    """
    if not isBadVersion(n)
    """
    end=n
    start =1
    while(start<=end):
        mid=start + (end-start) //2
        if isBadVersion(mid):
            end = mid-1
        else:
            start = mid+1
    if not isBadVersion(mid):
        return mid+1
    else:
        return mid


def isBadVersion(n):
    return n in badVersion

badVersion = [2,3]

print(firstBadVersion(7))