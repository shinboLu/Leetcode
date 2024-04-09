class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                checkleft = (i == 0) or (flowerbed[i-1] == 0)
                checkright = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

                if checkleft and checkright :
                    flowerbed[i] = 1
                    count += 1
        print(flowerbed)
        return count >= n

        