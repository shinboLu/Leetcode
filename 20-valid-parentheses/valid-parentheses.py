class Solution:
    def isValid(self, s: str) -> bool:

        counter = []
        mapping = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c not in mapping:
                counter.append(c)

            else: 
                if counter and counter[-1] == mapping[c]:
                    counter.pop()
                else:
                    return False
        return True if not counter else False