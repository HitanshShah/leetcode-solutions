class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    #     ans = []
    #     curr = []
    #     self.helper(nums, 0, ans, curr)
    #     return ans

    # def helper(self, nums, idx, ans, curr):
    #     print(curr, ans)
    #     if curr not in ans:
    #         ans.append(list(curr))
    #     if idx == len(nums):
    #         return
    #     curr.append(nums[idx])
    #     self.helper(nums, idx+1, ans, curr)
    #     curr.pop(-1)
    #     self.helper(nums,idx+1, ans, curr)

        ans = [[]]
        for num in nums:
            temp = []
            for a in ans:
                temp.append(a+[num])
            ans += temp
        return ans
                            