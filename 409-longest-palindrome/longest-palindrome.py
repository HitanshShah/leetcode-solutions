class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0)+1
        found_one = False
        for i in counts:
            if counts[i]%2 == 1:
                if not found_one:
                    found_one = True
                else:
                    n-=1
        return n