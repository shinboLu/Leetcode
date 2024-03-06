from heapq import heappop, heappush
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."

        for i in symbols:
            paragraph = paragraph.replace(i, " ")

        para_split = paragraph.split(' ')
        para_list = []

        for word in para_split:
            word = word.lower()
            if word.isalnum() and word not in banned:
                para_list.append(word)

        counter = collections.Counter(para_list)
        hq = []
        for k, v in counter.items():
            heappush(hq, (-v, k))
        while hq:
            val, key = heappop(hq) 
            return key 
