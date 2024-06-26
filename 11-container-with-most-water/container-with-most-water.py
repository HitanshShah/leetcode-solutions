class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        ans = 0
        # ans = min(height[left], height[right])*(right-left+1)
        while left < right:
            if min(height[left], height[right])*(right-left) > ans:
                ans = min(height[left], height[right])*(right-left)
            if height[left] <= height[right]:
                left+=1
            else:
                right-=1
        return ans