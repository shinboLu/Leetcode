class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = collections.Counter(word) 
        print(len(word))
        print(counter)

        frequency = [0] * 26

        for char in word:
            frequency[ord(char) - ord("a")] +=1

        frequency.sort(reverse=True) 

        total_tabs = 0 
        for i in range(26):
            if frequency[i] == 0:
                break
            total_tabs += (i//8+1) * frequency[i]

        return total_tabs