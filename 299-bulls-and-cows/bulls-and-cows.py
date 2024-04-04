class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        h = collections.Counter(secret)
            
        bulls = cows = 0
        for idx, ch in enumerate(guess):
            if ch in h:
                if ch == secret[idx]:
                    bulls += 1
                    cows -= int(h[ch] <= 0)
                # corresponding characters don't match
                else:
                    # update the cows
                    cows += int(h[ch] > 0)
                # ch character was used
                h[ch] -= 1

        return str(bulls) + 'A' + str(cows) + 'B'