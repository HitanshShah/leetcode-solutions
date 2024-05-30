class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pMap, sMap = {}, {}
        res = []
        for i in range(len(p)):
            pMap[p[i]] = 1+pMap.get(p[i],0)
            sMap[s[i]] = 1+sMap.get(s[i],0)
        if pMap == sMap:
            res.append(0)
        l = 0
        for r in range(len(p), len(s)):
            sMap[s[r]] = 1+sMap.get(s[r],0)
            sMap[s[l]] -= 1
            if sMap[s[l]] == 0:
                sMap.pop(s[l])
            l+=1
            if sMap == pMap:
                res.append(l)
        return res