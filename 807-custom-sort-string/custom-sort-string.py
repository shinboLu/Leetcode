class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        s_permutation = []

        for char in order:
            if char in freq:
                s_permutation.append(char * freq[char])
                del freq[char]

        for char in freq:
            s_permutation.append(char * freq[char])

        return ''.join(s_permutation)