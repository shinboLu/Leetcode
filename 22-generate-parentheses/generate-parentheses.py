class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      res = []
      def backtracking(left_count, right_count, comb):
        if len(comb) == 2 * n:
          res.append(''.join(comb))
          return
        if left_count < n:
          comb.append("(")
          backtracking(left_count+1, right_count, comb)
          comb.pop()
        if right_count < left_count:
          comb.append(")")
          backtracking(left_count, right_count+1, comb)
          comb.pop()
      backtracking(0,0,[])
      return res
