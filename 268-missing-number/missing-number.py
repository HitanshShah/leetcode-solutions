class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == len(nums):
        #         temp = nums[-1]
        #         nums[-1] = nums[i]
        #         nums[i] = temp
        #     else:
        #         # print(nums[i], i)
        #         temp = nums[nums[i]]
        #         nums[nums[i]] = nums[i]
        #         nums[i] = temp
        #     print(nums)
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return len(nums)


        n = len(nums)
        target = (n*(n+1))//2
        sums = 0
        for num in nums:
            sums += num
        return target - sums

        # n = len(nums)
        # return (n*(n+1)//2) - sum(nums)