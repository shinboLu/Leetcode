class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        strs.sort(key=len)
        shortest = strs[0]

        for i in range(len(shortest)):
            cur_char = shortest[i]

            for j in range(1, len(strs)):
                if strs[j][i] != cur_char:
                    return ''.join(res)
            res.append(cur_char)

        return ''.join(res)