class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        down = m-1
        right = n-1
        total = down + right
        ans = 1
        while total > max(down, right):
            ans *= total
            total -= 1
        den = min(down, right)
        div = 1
        while den > 0:
            div *= den
            den -= 1
        return ans//div