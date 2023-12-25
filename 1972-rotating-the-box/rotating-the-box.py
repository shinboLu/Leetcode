class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        nrow = len(box)
        ncol = len(box[0])


        for i in range(nrow):
            stone = 0
            for j in range(ncol):
                if box[i][j] == '#':
                    stone += 1
                    box[i][j] = '.'
                elif box[i][j] == '*':
                    for m in range(stone):
                        box[i][j-m-1] = '#'
                    stone = 0
            if stone != 0:
                for m in range(stone):
                    box[i][j-m] = '#'

        box[:]  = zip(*box[::-1])
        return box

        
