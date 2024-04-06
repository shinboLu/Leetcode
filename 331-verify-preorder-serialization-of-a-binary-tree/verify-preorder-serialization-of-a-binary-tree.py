class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preoder = preorder.split(',')
        avail = 1
        for node in preoder:
            avail -= 1

            if avail < 0:
                return False 

            if node != '#':
                avail += 2

        return avail == 0

