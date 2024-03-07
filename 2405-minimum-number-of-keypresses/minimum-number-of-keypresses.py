class Solution:
    def minimumKeypresses(self, s: str) -> int:

        counter = collections.Counter(s)

        frequency = list(counter.values())
        cur_count = 0
        res = 0
        for idx, value in enumerate(sorted(frequency, reverse= True)):
            if idx % 9 == 0:
                cur_count += 1
            res += cur_count * value
        return res 

