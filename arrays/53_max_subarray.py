#Medium

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Remove negative prefix - Sliding Window
        currSum = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            # If prefix is less than 0 , it is not adding anything to our value
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSum = max(currSum, maxSum)

        return maxSum

# Time Complexity: O(N)
# Space Complexity: O(1)

