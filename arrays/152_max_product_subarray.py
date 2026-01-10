#Medium
"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currMin, currMax = 1, 1

        for num in nums:
            if num == 0:
                currMin, currMax = 1, 1
                continue

            tmp = currMax * num
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(tmp, num * currMin, num)
            result = max(currMin, currMax, result)

        return result


# Time Complexity : O(n)
# Space Complexity : O(1)