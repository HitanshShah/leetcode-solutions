class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        l1, l2 = 0, 0
        while i>=0 or j>=0:
            while i >= 0:
                if s[i] == '#':
                    l1 += 1
                    i -= 1
                elif l1 > 0:
                    l1 -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == '#':
                    l2 += 1
                    j -= 1
                elif l2 > 0:
                    l2 -= 1
                    j -= 1
                else:
                    break
            if i>=0 and j >=0 and s[i] != t[j]:
                return False
            if((i>=0) != (j>=0)):
                return False
            i-=1
            j-=1
        return True
