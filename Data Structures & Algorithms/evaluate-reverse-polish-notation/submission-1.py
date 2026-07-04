class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = []
        for token in tokens:
            if token not in "+-*/":
                output.append(int(token))
            else:
                b = output.pop()
                a = output.pop()
                if token == "+":
                    output.append(a + b)
                elif token == "-":
                    output.append(a - b)
                elif token == "*":
                    output.append(a * b)
                else:
                    output.append(int(a / b))
        return output[-1]