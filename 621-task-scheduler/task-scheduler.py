class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0]*26
        for ch in tasks:
            counts[ord(ch)-ord("A")]+=1
        maxT = 0
        maxCount = 0
        for num in counts:
            if num > maxT:
                maxT = num
        for num in counts:
            if num == maxT:
                maxCount+=1
        return max(len(tasks), (maxT-1)*(n+1)+maxCount)