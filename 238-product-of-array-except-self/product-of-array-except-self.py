class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        ans = [1]*len(nums)
        for i in range(0,len(nums)-1):
            # if i == len(nums)-1:
            #     continue
            pre *= nums[i]
            ans[i+1] = pre
        for i in range(len(nums)-1, 0, -1):
            # if i == 0:
            #     continue
            post *= nums[i]
            ans[i-1] *= post
        return ans