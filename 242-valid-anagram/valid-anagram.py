class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0]*26
        for i in range(len(s)):
            counts[ord(s[i])-ord('a')]+=1
            counts[ord(t[i])-ord('a')]-=1
        for c in range(26):
            if counts[c]!=0:
                return False
        return True