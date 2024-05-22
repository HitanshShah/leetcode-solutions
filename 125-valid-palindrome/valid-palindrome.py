class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string = [c.lower() for c in s if c.isalnum()]
        # if string == string[::-1]:
        #     return True
        # else:
        #     return False
        start, end = 0, len(s)-1
        a = s.lower()
        while start < end:
            if not a[start].isalnum():
                start+=1
            elif not a[end].isalnum():
                end-=1
            elif a[start] == a[end]:
                start+=1
                end-=1
                # return False
            else:
                return False
        return True