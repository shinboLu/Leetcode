class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.token_time_map = collections.defaultdict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_time_map[tokenId] = currentTime + self.timeToLive
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.token_time_map:
            return

        if self.token_time_map[tokenId] > currentTime:
            self.token_time_map[tokenId] = currentTime + self.timeToLive
        else:
            del self.token_time_map[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        unexpriedToken = 0
        for key, val in self.token_time_map.items():
            if self.token_time_map[key] > currentTime:
                unexpriedToken += 1

        return unexpriedToken
                
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)