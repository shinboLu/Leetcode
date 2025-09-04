class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def validateIPv4(queryIP):
            splits = queryIP.split('.')
            
            for s in splits:
                if len(s) == 0 or len(s) > 3:
                    return "Neither"
                if s[0] == '0' and len(s) != 1:
                    return "Neither"
                
                if not s.isdigit():
                    return "Neither"
                
                if int(s) > 255:
                    return "Neither"
            return "IPv4"
        
        def validateIPv6(queryIP):
            splits = queryIP.split(':')
            hexadecimal = 'abcdefABCDEF0123456789'
            for s in splits:
                if len(s) == 0 or len(s) > 4:
                    return "Neither"
                
                for char in s:
                    if char not in hexadecimal:
                        return "Neither"
            return "IPv6"
        if queryIP.count('.') == 3:
            return validateIPv4(queryIP)
        elif queryIP.count(':') == 7:
            return validateIPv6(queryIP)
        else:
            return "Neither"