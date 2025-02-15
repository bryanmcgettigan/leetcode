def firstBadVersion(self, n):
    start=0
    end=n

    while start<=end:
        mid=(start+end)//2

        if isBadVersion(mid):
            end = mid-1
        else:
            start=mid+1
    return start


def isBadVersion(num):
    return True