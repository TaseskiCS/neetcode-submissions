class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            product = 1 # initialize a product to be able to multiply with
            for j in range(len(nums)): # start other loop to go through same list
                if i != j: # make sure we dont include the current index in the multiplication
                    product *= nums[j] 
            
            result.append(product)
        return result

            
            
            