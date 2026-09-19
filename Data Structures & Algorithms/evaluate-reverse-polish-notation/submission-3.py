class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set("+-*/")
        for i in tokens:
            # print(stack)
            if i in operators:
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                if i == "+":
                    stack.append(op1 + op2)
                    continue
                if i == "-":
                    stack.append(op1 - op2)
                    continue
                if i == "*":
                    stack.append(op1 * op2)
                    continue
                if i == "/":
                    stack.append(int(op1 / op2))
                    continue
            else:
                stack.append(int(i))
        return stack[-1]
        