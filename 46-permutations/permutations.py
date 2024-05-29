class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        self.permutations(ans, nums, curr)
        return ans

    def permutations(self, ans, nums, curr):
        if len(curr) == len(nums):
            ans.append(list(curr))
            return
        for i in range(len(nums)):
            if nums[i] in curr:
                continue
            curr.append(nums[i])
            self.permutations(ans, nums, curr)
            curr.pop()
        return