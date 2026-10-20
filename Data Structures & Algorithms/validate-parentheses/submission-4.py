class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            else:
                if stack:
                    current = stack.pop()
                    if current == '(' and i != ')':
                        return False
                    elif current == '[' and i != ']':
                        return False
                    elif current == '{' and i != '}':
                        return False
                else:
                    return False 
        if stack:
            return False
        return True