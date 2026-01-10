#Easy
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        result = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                result.append(hashmap[complement])
                result.append(i)
                return result
            else:
                hashmap[nums[i]] = i
        return result

# Time Complexity : O(n)
# Space Complexity : O(n)