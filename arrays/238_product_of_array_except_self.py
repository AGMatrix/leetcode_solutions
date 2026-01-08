class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        pre_accum = 1
        for num in nums:
            result.append(pre_accum)
            pre_accum *= num

        post_accum = 1
        for i in range(len(nums) - 1, -1, -1):
            value = result[i] * post_accum
            result[i] = value
            post_accum *= nums[i]

        return result


# Time Complexity : O(n)
# Space Complexity : O(1) (excluding the output array)