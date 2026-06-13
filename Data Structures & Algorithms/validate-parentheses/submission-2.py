class Solution: 
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '[':
                stack.append(char)
            elif char == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif char == '{':
                stack.append(char)
            elif char == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
        return not stack