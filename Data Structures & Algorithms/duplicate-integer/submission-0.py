class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked_array = set(nums)
        if len(nums) != len(checked_array):
            return True
        return False
