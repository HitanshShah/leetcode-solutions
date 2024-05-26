class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n1 = len(strs[0])-1
        n2 = len(strs[-1])-1
        i, j = 0, 0
        while i<=n1 and j<=n2:
            if strs[0][i] == strs[-1][j]:
                i+=1
                j+=1
            else:
                break
        if i>0:
            return strs[0][:i]
        else:
            return ""