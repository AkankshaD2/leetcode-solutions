class Solution(object):
    def isGood(self, nums):
        nums.sort()
        n = nums[-1]
        if len(nums) != n + 1:
            return False
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False
        return nums[-1] == n and nums[-2] == n
