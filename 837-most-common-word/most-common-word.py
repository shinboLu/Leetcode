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
            print(word)
            if word.isalnum() and word not in banned:
                para_list.append(word)

        counter = collections.Counter(para_list)
        print(counter)
        hq = []
        for k, v in counter.items():
            heappush(hq, (-v, k))
        print(hq)
        while hq:
            val, key = heappop(hq) 
            return key 


# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         # first we need to remove the symbols that can be present, and replacing with space
#         symbols = "!?',;."
#         for i in symbols:
#             paragraph = paragraph.replace(i, " ")
#         hashMap = defaultdict(int)
#         # converting to lower case
#         paragraph = paragraph.lower()
#         # splitting based on space to put the given words to a list
#         list1 = paragraph.split()

#         # checking if the word not in banned , and incrementing its count
#         for i in list1:
#             if i not in banned:
#                 hashMap[i] = hashMap[i] + 1

#         # finding the word has occurs most number of times
#         maximum = max(hashMap.values())

#         # finding the value of key for the word with maximum count
#         for key, value in hashMap.items():
#             if value == maximum:
#                 return key
