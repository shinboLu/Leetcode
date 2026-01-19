class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        counter = collections.Counter()

        left = 0 

        for right in range(len(fruits)):
            counter[fruits[right]] +=1

            while len(counter.keys()) > 2:
                counter[fruits[left]] -= 1
                if counter[fruits[left]] == 0:
                    del counter[fruits[left]]
                left +=1

            res = max(res, sum(counter.values()))
        return res
        