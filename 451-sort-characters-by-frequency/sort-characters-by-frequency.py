class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        pairs = sorted(
            counter.items(),
            key=lambda pair: pair[1],
            reverse=True
        )

        return "".join(char * count for char, count in pairs)
        

