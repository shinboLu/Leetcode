class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        plates = [0] * len(s)
        count = 0
        for i, ch in enumerate(s):
            if ch == '*':
                count += 1
            plates[i] = count

        for i in range(len(s)):
            if s[i] == '|':
                candles.append(i)
        
        def binary_search(left, right):
            left_b = bisect.bisect_left(candles, left)
            right_b = bisect.bisect_right(candles, right)-1
            return [left_b, right_b]

        res = []
        for start, end in queries:
            cur_left, cur_right = binary_search(start, end)

            if cur_left == len(candles) or cur_right < 0 or cur_left > cur_right:
                res.append(0)
                continue

            left_candle = candles[cur_left]
            right_candle = candles[cur_right]

            if left_candle >= right_candle:
                res.append(0)
            else:
                res.append(plates[right_candle] - plates[left_candle])

        return res