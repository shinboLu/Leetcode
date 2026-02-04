class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        mapping = collections.defaultdict(int)
        res = 0
        left = 0 

        for right in range(len(fruits)):
            mapping[fruits[right]] +=1

            while len(mapping) > 2:
                mapping[fruits[left]] -=1
                if mapping[fruits[left]] == 0:
                    del mapping[fruits[left]]
                left +=1
            res = max(res, sum(mapping.values()))

        return res