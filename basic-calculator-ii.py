DIGITS = "0123456789"

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        num = 0
        sign = "+"
        stack = []

        for i, char in enumerate(s):
            if char in DIGITS:
                num = num * 10 + ord(char) - ord("0")            
            
            if char in "+-*/" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)

                elif sign == "-":
                    stack.append(-1 * num)

                elif sign == "*":
                    stack.append(stack.pop() * num)

                elif sign == "/":
                    if stack[-1] >= 0:
                        stack.append(stack.pop() // num)
                    else:
                        stack.append(-1 * stack.pop() // num * -1)

                sign = char
                num = 0

        return sum(stack)
