# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        first_bad = 0
        while start <= end:
            mid = (start + end)//2
            if isBadVersion(mid):
                first_bad = mid
                end = mid-1
            else:
                start = mid+1
        return first_bad