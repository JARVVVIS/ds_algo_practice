class Solution:

    def rec(self,N,vals):
        if N in vals.keys():
            return vals[N]
        else:
            ans = self.rec(N-1,vals)+self.rec(N-2,vals)
            vals[N] = ans
            return ans
    
    def fib(self,N : int) -> int:
        vals = {0:0,1:1}
        ans = self.rec(N,vals)
        return ans



if __name__ == '__main__':
    sol = Solution()
    print(sol.fib(30))