class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_numbers = list(set(nums))
        return not (len(unique_numbers) == len(nums))