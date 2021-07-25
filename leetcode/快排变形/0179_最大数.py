class Solution:
    def largestNumber(self, nums) -> str:
        def partitions_v2(strs, left, right):
            base = strs[left]

            while left < right:
                while left < right and strs[right] + base <= base + strs[right]: right -= 1
                strs[left] = strs[right]
                while left < right and strs[left] + base >= base + strs[left]: left += 1
                strs[right] = strs[left]
            strs[left] = base
            return left

        def quick_sort(strs, left, right):
            if left < right:
                mid = partitions_v2(strs, left, right)
                quick_sort(strs, left, mid - 1)
                quick_sort(strs, mid + 1, right)

        strs = [str(num) for num in nums]
        quick_sort(strs, 0, len(nums) - 1)

        return "0" if strs[0] == "0" else "".join(strs)
