class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        num = x
        while num != 0:
            rev = rev*10 + num%10
            num = num//10
        if rev == x:
            return True
        else:
            return False
