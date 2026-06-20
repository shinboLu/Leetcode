import collections

class Solution:
    def longestBalanced(self, s: str) -> int:
        def calc1(s):
            # Longest single-character run
            res = i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                res = max(res, j - i)
                i = j
            return res

        def calc2(s, a, b):
            # Longest substring with only a and b, equal counts
            res, i, n = 0, 0, len(s)
            while i < n:
                while i < n and s[i] != a and s[i] != b:
                    i += 1
                seen = {0: i - 1}
                d = 0
                while i < n and (s[i] == a or s[i] == b):
                    d += 1 if s[i] == a else -1
                    if d in seen:
                        res = max(res, i - seen[d])
                    else:
                        seen[d] = i
                    i += 1
            return res

        def calc3(s):
            # Longest substring with equal counts of a, b, c
            res = 0
            seen = {(0, 0): -1}
            ca = cb = cc = 0
            for i, ch in enumerate(s):
                if ch == 'a': ca += 1
                elif ch == 'b': cb += 1
                else: cc += 1
                state = (ca - cb, cb - cc)
                if state in seen:
                    res = max(res, i - seen[state])
                else:
                    seen[state] = i
            return res

        return max(
            calc1(s),
            calc2(s, 'a', 'b'),
            calc2(s, 'a', 'c'),
            calc2(s, 'b', 'c'),
            calc3(s)
        )