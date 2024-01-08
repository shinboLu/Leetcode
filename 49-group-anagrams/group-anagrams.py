from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) <= 1:
            return [strs]

        counter = collections.defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            counter[sorted_s].append(s) 

        res = []

        for k, v in counter.items():
            res.append(v)

        return res 