class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        max_li = collections.deque()
        min_li = collections.deque()
        res = []
        for num in nums:
            if num >= 0:
                max_li.append(num)
            else:
                min_li.append(num)
        print(max_li, min_li)
        while max_li and min_li:
            res.append(max_li.popleft())
            res.append(min_li.popleft())

        return res