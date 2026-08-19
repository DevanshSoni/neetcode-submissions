class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        traversed_items = {}
        for index, item in enumerate(nums):
            number = target - item
            if number in traversed_items:
                return [traversed_items[number], index]

            traversed_items[item] = index
