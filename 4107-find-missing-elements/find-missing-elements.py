class Solution(object):
    def findMissingElements(self, nums):
        s = set(nums)
        smallest = min(nums)
        largest = max(nums)

        ans = []

        for num in range(smallest , largest + 1):
             if num not in s:
                ans.append(num)

        return ans        

        