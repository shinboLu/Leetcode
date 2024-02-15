class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        p_s_map = {}

        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if s[i] in p_s_map.values():
                continue
            elif pattern[i] not in p_s_map:
                p_s_map[pattern[i]] = s[i]

        new_str = []

        for p in pattern:
            new_str.append(p_s_map.get(p, '0'))

        return new_str == s
