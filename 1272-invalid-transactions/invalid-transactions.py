from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        hashmap = defaultdict(list)
        res = set()

        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')

            if name not in hashmap:
                if int(amount) > 1000:
                    res.add(i)

            else:
                prevTrans = hashmap[name]

                for j in range(len(prevTrans)):
                    prevName, prevTime, prevAmount, prevCity = transactions[prevTrans[j]].split(',')
                    if int(amount) > 1000:
                        res.add(i)

                    if abs(int(time) - int(prevTime)) <= 60 and city != prevCity:
                        res.add(i)
                        res.add(prevTrans[j])

            hashmap[name].append(i)

        return [transactions[t] for t in res] 


