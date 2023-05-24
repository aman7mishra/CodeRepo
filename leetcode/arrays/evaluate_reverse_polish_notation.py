class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '/', '*']
        for n in tokens:
            if n in operators:
                second, first = stack.pop(), stack.pop()
                if n == "+":
                    stack.append(first+second)
                elif n == "-":
                    stack.append(first-second)
                elif n == '*':
                    stack.append(first*second)
                else:
                    stack.append(int(first/second))
            else:
                stack.append(int(n))
        return stack[0]