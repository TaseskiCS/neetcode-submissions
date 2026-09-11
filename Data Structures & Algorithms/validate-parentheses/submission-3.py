class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ["[", "{", "("]
        stack = []
        for i in s:
            if i in open_brackets:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if i == '}':
                    if stack.pop() != '{':
                        return False
                elif i == ']':
                    if stack.pop() != '[':
                        return False
                elif i == ')':
                    if stack.pop() != '(':
                        return False
        if len(stack) != 0:
            return False

        return True