class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter, w = collections.Counter(s1), len(s1)   

        for i in range(len(s2)):
            if s2[i] in counter: 
                counter[s2[i]] -= 1
            if i >= w and s2[i-w] in counter: 
                print(s2[i-w])
                counter[s2[i-w]] += 1

            if all([counter[i] == 0 for i in counter]): 
                return True

        return False