class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        valid_ops = set(["+", "-", "*", "/"])
        for token in tokens:
            if token in valid_ops:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "/":
                    tmp = first / second
                    if tmp < 0:
                        tmp = math.ceil(tmp)
                    else:
                        tmp = math.floor(tmp)
                    stack.append(tmp)
                elif token == "*":
                    stack.append(first * second)
            else:
                stack.append(int(token))
        ret = stack.pop()
        return ret
    