class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort() 
        res = []
        cur = ''
        cur_idx = 0
        for c in searchWord:
            cur+=c
            insert_idx = bisect.bisect_left(products, cur, cur_idx)
            res.append([w for w in products[insert_idx:insert_idx+3] if w.startswith(cur)])

        return res

