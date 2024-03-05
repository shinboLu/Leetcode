class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse= True) 
        s.sort(reverse = True)
        print(g, s)
        gp = 0 
        sp = 0
        res = 0

        while gp< len(g) and sp < len(s):
            if g[gp] <= s[sp]:
                res += 1
                gp+=1
                sp+=1
            else:
                gp+=1

        return res 


