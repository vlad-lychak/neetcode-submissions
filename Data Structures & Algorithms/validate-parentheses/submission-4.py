class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parent = {
            "]":"[",
            ")":"(",
            "}":"{"
        }

        for c in s:
            if c in parent:
                if stack and stack[-1] == parent[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        

        if stack:
            return False
        else:
            return True