# from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # if len(ransomNote) > len(magazine):
        #     return False
        # mag_counts = Counter(magazine)
        # for c in ransomNote:
        #     if not mag_counts[c]:
        #         return False
        #     elif mag_counts[c] <= 0:
        #         return False
        #     else:
        #         mag_counts[c] -= 1
        # return True
        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False
        return True