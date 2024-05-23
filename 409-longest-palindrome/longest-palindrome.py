class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = 0
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0)+1
        found_one = False
        for i in counts:
            if counts[i]%2 == 1:
                if not found_one:
                    found_one = True
                n+=counts[i]-1
            else:
                n+=counts[i]
        if found_one:
            return n+1
        else:
            return n