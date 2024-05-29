class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 == 1:
            return False
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            tempDP = set(dp)
            for t in dp:
                tempDP.add(t+nums[i])
            dp = tempDP
            if target in dp:
                return True
        return False
