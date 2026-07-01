class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) + int(second))
            elif t == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) - int(second))
            elif t == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) * int(second))                
            elif t == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) / int(second))
            else:
                stack.append(t)

        return int(stack[0])