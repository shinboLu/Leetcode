class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = collections.defaultdict(list)
        res = []
        for val in strs:
            sorted_val = ''.join(sorted(val))

            if sorted_val not in mapping.keys():
                mapping[sorted_val] = []
            mapping[sorted_val].append(val)

        for k in mapping:
            res.append(mapping[k])
        
        return res

