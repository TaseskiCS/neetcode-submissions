class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t = {}

        for i in s:
            if i in letters_s:
                letters_s[i] +=1
            else:
                letters_s[i] = 1
        for i in t:
            if i in letters_t:
                letters_t[i] += 1
            else:
                letters_t[i] = 1

        if letters_s == letters_t:
            return True

        return False