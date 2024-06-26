class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans = []
        ans.append(0)
        for i in range(1, n+1):
            if i%2 == 0:
                ans.append(ans[i//2])
            else:
                ans.append(ans[i-1]+1)
        return ans