class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            remainder = target - nums[i]

            if remainder in nums[i+1:]:
                return [i, nums.index(remainder, i + 1)]

        return False