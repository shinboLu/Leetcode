class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []

        for s in strs:
            sorted_strs.append(''.join(sorted(s)))
        mapping = collections.defaultdict(list)

        for i in range(len(sorted_strs)):
            mapping[sorted_strs[i]].append(strs[i])
        res = []
        for k, v in mapping.items():
            res.append(v)

        return res

                