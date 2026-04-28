class Solution(object):
    def minOperations(self, grid, x):
        nums = []
        for row in grid:
            for val in row:
                nums.append(val)
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1  
        nums.sort()
        median = nums[len(nums) // 2]
        operations = 0
        for num in nums:
            operations += abs(num - median) // x
        
        return operations
