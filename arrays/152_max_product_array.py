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