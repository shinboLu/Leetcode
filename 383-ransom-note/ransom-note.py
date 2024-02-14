class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_counter = collections.Counter(ransomNote)
        mag_counter = collections.Counter(magazine)

        for k, v in note_counter.items():
            if k not in mag_counter or v > mag_counter[k]:
                return False
        return True 
