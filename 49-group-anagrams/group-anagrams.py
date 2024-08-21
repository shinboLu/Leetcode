from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
    

        res = [] 
        word_map = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            word_map[sorted_word].append(word)

        for key, value in word_map.items():
            res.append(value)

        return res