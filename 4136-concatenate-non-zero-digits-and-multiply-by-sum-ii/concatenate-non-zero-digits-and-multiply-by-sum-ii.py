class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # for each position, store digit and whether it's non-zero
        # prefix_sum[i] = sum of non-zero digits in s[0:i]
        prefix_sum = [0] * (n + 1)
        # prefix_num[i] = numeric value formed by non-zero digits in s[0:i] mod MOD
        prefix_num = [0] * (n + 1)
        # count of non-zero digits up to position i
        prefix_nz_count = [0] * (n + 1)

        for i, ch in enumerate(s):
            d = int(ch)
            prefix_nz_count[i+1] = prefix_nz_count[i] + (1 if d != 0 else 0)
            prefix_sum[i+1] = prefix_sum[i] + d
            prefix_num[i+1] = (prefix_num[i] * 10 + d) % MOD if d != 0 else prefix_num[i]

        # pow10[i] = 10^i mod MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = pow10[i-1] * 10 % MOD

        res = []
        for start, end in queries:
            digit_sum = prefix_sum[end+1] - prefix_sum[start]
            if digit_sum == 0:
                res.append(0)
                continue

            # number of non-zero digits in window
            nz_count = prefix_nz_count[end+1] - prefix_nz_count[start]

            # numeric value of non-zero digits in window
            # prefix_num[end+1] contains non-zero digits from 0..end
            # prefix_num[start] contains non-zero digits from 0..start-1
            # shift prefix_num[start] left by nz_count positions
            num_val = (prefix_num[end+1] - prefix_num[start] * pow10[nz_count]) % MOD

            res.append((digit_sum * num_val) % MOD)

        return res