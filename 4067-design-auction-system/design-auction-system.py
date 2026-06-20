from heapq import heapify, heappush, heappop
from sortedcontainers import SortedList

class AuctionSystem:

    def __init__(self):
        self.system = collections.defaultdict(lambda : collections.defaultdict(int))
        self.heap = collections.defaultdict(list)
    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.system[itemId][userId] = bidAmount
        temp_bid = [-bidAmount, -userId]
        heappush(self.heap[itemId], temp_bid)

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.system[itemId][userId] = newAmount
        temp_bid = [-newAmount, -userId]
        heappush(self.heap[itemId], temp_bid)

    def removeBid(self, userId: int, itemId: int) -> None:
        del self.system[itemId][userId]

    def getHighestBidder(self, itemId: int) -> int:
        while self.heap[itemId]:
            price, user_id = self.heap[itemId][0]
            price = -price
            user_id = -user_id
            if self.system[itemId][user_id]!= price:
                heappop(self.heap[itemId])
                continue
            return user_id
        return -1



# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)