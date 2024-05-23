class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        found_one = False
        for c in set(s):
            if s.count(c)%2 == 1:
                if not found_one:
                    found_one = True
                else:
                    n-=1
        return n