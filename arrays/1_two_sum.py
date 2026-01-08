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