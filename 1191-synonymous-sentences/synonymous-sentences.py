from collections import defaultdict
class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph = defaultdict(list)
        for n1, n2 in synonyms:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        word_to_syn = defaultdict(set)

        def dfs(word):
            if word in syns:
                return
            syns.add(word)
            for edge in graph[word]:
                dfs(edge)
        
        for key in graph.keys():
            syns = set()
            dfs(key)
            word_to_syn[key] = syns
        
        sentence = text.split()
        ans = []

        def backtrack(i):
            if i == len(sentence):
                ans.append(' '.join(sentence))
                return
            curr_word = sentence[i]
            if curr_word in word_to_syn:
                for syn in word_to_syn[curr_word]:
                    sentence[i] = syn
                    backtrack(i + 1)
                    sentence[i] = curr_word
            else:
                backtrack(i + 1)
        
        backtrack(0)
        ans.sort()
        return ans


                        

        
        





        
                        
                    

            
                        

            

        