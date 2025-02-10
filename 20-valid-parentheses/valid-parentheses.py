class Solution:
    def isValid(self, s: str) -> bool:
        pair = []

        mapping = {")":"(", "}": "{", "]":"["}

        for char in s: 
            if char not in mapping:
                pair.append(char)
            else:
                if pair and pair[-1] == mapping[char]:
                    pair.pop()
                else:
                    return False

        return True if not pair else False
            