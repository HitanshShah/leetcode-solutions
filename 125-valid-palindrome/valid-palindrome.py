class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [c.lower() for c in s if c.isalnum()]
        if string == string[::-1]:
            return True
        else:
            return False