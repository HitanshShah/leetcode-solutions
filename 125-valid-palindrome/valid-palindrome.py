class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string = [c.lower() for c in s if c.isalnum()]
        # if string == string[::-1]:
        #     return True
        # else:
        #     return False
        start, end = 0, len(s)-1
        while start < end:
            if not s[start].isalnum():
                start+=1
                continue
            if not s[end].isalnum():
                end-=1
                continue
            if s[start].lower() != s[end].lower():
                return False
            else:
                start+=1
                end-=1
        return True