from string import ascii_lowercase

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dic = collections.defaultdict(list)

        for string in strs:
            sorted_string = ''.join(sorted(string))
            sorted_dic[sorted_string].append(string)

        return sorted_dic.values()

