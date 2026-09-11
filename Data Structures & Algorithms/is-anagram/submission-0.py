class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        letters_s = {}
        letters_t = {}

        for letter in s:
            if letter in letters_s:
                letters_s[letter] +=1
            else:
                letters_s[letter] = 1
        for letter in t:
            if letter in letters_t:
                letters_t[letter] +=1
            else:
                letters_t[letter] = 1

        if letters_s == letters_t: 
            return True

        return False
            