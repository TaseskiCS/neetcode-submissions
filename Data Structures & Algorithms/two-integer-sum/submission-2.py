class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {} 
        i = 0
        while i < len(nums):
            comp = target - nums[i] #take complement from target - curr val @ index

            if comp not in temp:
                temp[nums[i]] = i #add val into hashmap with key of index
            else:
                return [temp[comp], i] #return indexed vals index with curr index
            i+=1

            