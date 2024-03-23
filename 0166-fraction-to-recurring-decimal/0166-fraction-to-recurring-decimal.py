class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        if denominator == 1:
            return str(numerator)
        
        fraction = []
        is_negative = numerator * denominator < 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        q = numerator // denominator
        rem = numerator % denominator
        fraction.append(str(q))
        if rem == 0:
            return "".join(fraction)
        
        fraction.append(".")
        numerator = rem * 10
        index = 2
        mem = {
            numerator: index
        }
        open_index = -1
        while rem != 0:
            q = numerator // denominator
            rem = numerator % denominator
            fraction.append(str(q))
            numerator = rem * 10
            if numerator in mem:
                fraction.append(")")
                open_index = mem[numerator]
                break
            index += 1
            mem[numerator] = index
        ret = []
        if is_negative:
            ret.append("-")
        for i, ch in enumerate(fraction):
            if i == open_index:
                ret.append("(")
            ret.append(ch)
        return "".join(ret)
