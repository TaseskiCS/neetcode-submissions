class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        streak = set(nums)
        longest_sequence = 0
        for i in streak:
            # check if start of sequence
            check = i - 1 #check if has no left neighbour
            if check not in streak:
                length = 0 # start of sequence
                while (i + length) in streak: # checks if our current + length is in the set eg. 2 + length(1) = 3, in the set
                    length += 1
                longest_sequence = max(length, longest_sequence) #take the longest sequence from set and current longest
                
        return longest_sequence