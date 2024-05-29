class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        ans = []
        currStart = 0
        currEnd = 0
        for start, end in intervals:
            if not ans:
                ans.append([start, end])
                currStart = start
                currEnd = end
                continue
            if currStart <= start <= currEnd:
                currEnd = max(end, currEnd)
                ans[-1][1] = currEnd
            else:
                currStart = start
                currEnd = end
                ans.append([currStart, currEnd])
        return ans