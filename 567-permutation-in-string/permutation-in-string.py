class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter, w = collections.Counter(s1), len(s1)
        n = 0
        while n + w <= len(s2):
            if s2[n] in counter:
                s2_sub_string_counter = collections.Counter(s2[n:n+w])
                #print(s2_sub_string_counter)
                if counter == s2_sub_string_counter:
                    return True
            n += 1


        return False