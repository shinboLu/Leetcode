class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0 
        write_idx = 0
        while left < len(chars):
            right = left
            cur_count = 0 
            while right < len(chars) and chars[right] == chars[left]:
                right +=1
                cur_count +=1

            chars[write_idx] = chars[left]
            write_idx+=1

            if cur_count > 1:
                for digit in str(cur_count):
                    chars[write_idx] = digit
                    write_idx +=1
            left = right
        return write_idx
