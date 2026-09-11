class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        count = 0                       ## lets use [3,4,5,6] eg.
        while count < len(nums):
            complement = target - nums[count]
            ## first iteration value = 3 index = 0
            ## will be added as {3 : 0}, second: { 
                                        ##        3 : 0,
                                        ##        4 : 1      
                                        ##      } 
            if complement not in temp:
                temp[nums[count]] = count
            else:

                # since 7 - 4 = 3 is in temp as we see ^^^^(3 : 0)

                # it returns the 0 part of it which is the index
                # along with its current index of 1
                return [temp[complement], count]
            count +=1

            