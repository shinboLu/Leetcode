class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s, counter_t = collections.Counter(s), collections.Counter(t)
        if len(s) != len(t):
            return False
        for k, v in counter_s.items():
            print(k,v)
            if k in counter_t.keys() and counter_t[k] == v:
                continue
            else:
                return False
        return True
