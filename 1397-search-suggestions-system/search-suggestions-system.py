class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        cur = ''
        res = []
        cur_idx = 0 
        for char in searchWord:
            cur += char
            idx = bisect.bisect_left(products, cur, cur_idx)
            res.append([w for w in products[idx:idx+3] if w.startswith(cur)]) 
            cur_idx = idx

        return res