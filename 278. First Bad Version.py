def isBadVersion(version):

class Solution:
    def firstBadVersion(n):
        left, right = 0, n

        while left < right:
            mid =(right + left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return right
