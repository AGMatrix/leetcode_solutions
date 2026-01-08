#Easy
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)

        return not (len(set_nums) == len(nums))


# Time Complexity : O(n)
# Space Complexity : O(n)



