class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        nums_key = sorted(list(counter.keys()))
        earn1, earn2 = 0, 0

        for i in range(len(nums_key)):
            curEarn = nums_key[i] * counter[nums_key[i]]
            if i > 0 and nums_key[i] == nums_key[i-1]+1:
                temp = earn2
                earn2 = max(curEarn + earn1, earn2)
                earn1 = temp

            else:
                temp = earn2
                earn2 = curEarn + earn2
                earn1 = temp
                

        return earn2


        