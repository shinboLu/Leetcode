class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ## plates[i]: for child i, he has # of cookies
        plates = [0] * k

        n = len(cookies)

        def place_cookies(cookie_index, empty_plates):
            ## trimming: if there are less cookies than k, terminate

            if n - cookie_index < empty_plates:
                return float('inf')

            ## base case 2: if distributed all cookies, return the max 
            ##      total cookies obtained by a single child in the distribution
            if cookie_index == n:
                return max(plates)

            res = float('inf')
            ## maintainance

            for i in range(k):
                ## if the ith kid has cookie, reduce the number of total empty plates by 1
                empty_plates -= int(plates[i] == 0)

                plates[i] += cookies[cookie_index]
                res = min(res, place_cookies(cookie_index+1, empty_plates))
                plates[i] -= cookies[cookie_index]
                empty_plates += int(plates[i] == 0)
                

            return res 

        return place_cookies(0, k)
        

