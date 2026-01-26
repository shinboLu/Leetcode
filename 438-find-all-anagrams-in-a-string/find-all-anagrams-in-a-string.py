class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        res = []

        counter_s = collections.defaultdict(int)
        counter_p = collections.Counter(p)

        for i in range(len(s)):
            counter_s[s[i]] += 1

            if i >= len_p:
                if counter_s[s[i-len_p]]==1:
                    del counter_s[s[i-len_p]]
                else:
                    counter_s[s[i-len_p]] -=1
            if counter_p == counter_s:
                res.append(i-len_p+1)

        return res
            

