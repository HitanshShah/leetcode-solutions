class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        # while i<len(nums):
        #     if nums[i] == 0:
        #         if i == len(nums)-1:
        #             break
        #         j = i
        #         while(j < len(nums)-1 and nums[j] == 0):
        #             j+=1
        #         temp = nums[j]
        #         nums[j] = nums[i]
        #         nums[i] = temp
        #     i+=1
        for j in range(len(nums)):
            if nums[j] != 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i+=1