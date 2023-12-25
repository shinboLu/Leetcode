class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace('))', '}')
        missing_bracket = 0
        required_closed = 0

        for ch in s:
            if ch == '(':
                required_closed += 2
            else:
                if ch == ')':
                    missing_bracket += 1

                if required_closed != 0:
                    required_closed -= 2

                else:
                    missing_bracket += 1
        return missing_bracket + required_closed