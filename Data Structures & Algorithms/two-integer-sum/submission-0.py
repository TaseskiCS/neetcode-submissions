class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        count = 0
        while count < len(nums):
            complement = target - nums[count]
            if complement in temp:
                return [temp[complement], count]
            else:
                temp[nums[count]] = count
            count +=1
            