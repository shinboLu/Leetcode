class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        frequency = list(counter.values())
        frequency.sort(reverse=True)
        res = set()
        for i in frequency[:k]:
            for k,v in counter.items():
                if v == i:
                    res.add(k)
        return res 

            


        