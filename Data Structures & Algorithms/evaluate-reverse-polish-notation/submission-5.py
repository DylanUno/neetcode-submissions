class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            elif i in ["+", "-", "*", "/"]:
                b, a = stack.pop(), stack.pop()
                if i == "+":
                    stack.append(a + b)

                elif i == "-":
                    stack.append(a - b)

                elif i == "*":
                    stack.append(a * b)

                elif i == "/":
                    stack.append(int(a / b))
        
        return stack.pop()
            
        