class Solution:
    def subsets(self, nums):
        if len(nums) == 0: return [[]]

        ans = [[nums[0]]]

        for i in range(1, len(nums)):
            ans = ans + [t + [nums[i]] for t in ans] + [[nums[i]]]

        return ans + [[]]


s = Solution()
s.subsets([1, 2, 3])
