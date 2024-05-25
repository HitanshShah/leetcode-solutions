class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        for i in range(len(s)):
            if s[i] in ['I', 'X', 'C']:
                if s[i] == 'I':
                    if i < len(s)-1 and s[i+1] in ['V', 'X']:
                        num -= mapping[s[i]]
                        continue
                elif s[i] == 'X':
                    if i < len(s)-1 and s[i+1] in ['L', 'C']:
                        num -= mapping[s[i]]
                        continue
                else:
                    if i < len(s)-1 and s[i+1] in ['D', 'M']:
                        num -= mapping[s[i]]
                        continue
            num += mapping[s[i]]
        return num