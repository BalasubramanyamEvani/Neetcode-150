class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        N = len(tokens)
        l = 0
        r = N - 1
        score = 0
        while l <= r:
            if tokens[l] <= power:
                score += 1
                power -= tokens[l]
                l += 1
            elif score >= 1:
                if l != r:
                    score -= 1
                    power += tokens[r]
                r -= 1
            else:
                break
        return score
