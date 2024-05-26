class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        start = 0
        end = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[start]) > abs(nums[end]):
                ans[i] = nums[start]**2
                start+=1
            else:
                ans[i] = nums[end]**2
                end-=1
        return ans
