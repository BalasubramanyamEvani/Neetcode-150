class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op == "+":
                ns = sum(scores[-2:])
                scores.append(ns)
            elif op == "D":
                ns = scores[-1] * 2
                scores.append(ns)
            elif op == "C":
                scores.pop()
            else:
                scores.append(int(op))
        res = sum(scores)
        return res
        