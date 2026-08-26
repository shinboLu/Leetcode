class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s) 

        flat_counter = [[val, count] for val, count in counter.items()]
        flat_counter.sort(key = lambda x: x[1], reverse=True )
        res = ''
        for k, v in flat_counter:
            cur_str = k*v
            res+=cur_str

        return res
        

