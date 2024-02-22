from string import ascii_lowercase
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append([beginWord, 1])
        wordList = set(wordList)
        visited = set(beginWord)  

        while queue:
            cur_word, cur_cnt = queue.popleft()
            if cur_word == endWord:
                return cur_cnt
            for i in range(len(cur_word)):
                for j in ascii_lowercase:
                    temp = cur_word[:i] + j + cur_word[i+1:]

                    if temp not in visited and temp in wordList:
                        visited.add(temp)
                        queue.append([temp, cur_cnt+1])
        return 0

