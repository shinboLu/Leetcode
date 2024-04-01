class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs = [
            ['0','0'], ['1', '1'], ['6', '9'], ['8', '8'], ['9', '6']
            ]

        def generate_strobo_numbers(num, final_len):
            print(num)
            if num == 0:
                return ['']

            if num == 1:
                return ['0', '1', '8']

            prev_nums = generate_strobo_numbers(num-2, final_len)
            curr_strobo_nums = []

            for p in prev_nums:
                for pair in pairs:
                    if pair[0] != '0' or num != final_len:
                        curr_strobo_nums.append(pair[0] + p + pair[1])
            return curr_strobo_nums
        return generate_strobo_numbers(n, n)

            
