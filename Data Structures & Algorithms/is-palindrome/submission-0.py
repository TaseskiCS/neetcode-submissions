class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''
        valid = True
        i=0
        if len(s) == 0:
            valid = True

        for char in s:
            if char.isalnum():
                temp+=char.lower()

        left = 0
        right = len(temp)-1

        while left < right:
            if temp[left] != temp[right]:
                valid = False
            left +=1
            right -=1
        return valid