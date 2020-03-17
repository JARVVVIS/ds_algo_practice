# Count the number of prime numbers less than a non-negative number, n.

class Solution:

    def get_primes(self,n):
        lp = [0]*(n+1)
        primes = []
        for val in range(2,n+1):
            if not lp[val]:
                lp[val] = val 
                primes.append(val)
            j = 0
            while j<len(primes) and val*primes[j]<=n and primes[j]<=lp[val*primes[j]]:
                lp[val*primes[j]] = j 
                j+=1
        ans=0
        for prime in primes:
            if prime<n:
                ans+=1
            else:
                return ans
        return ans




    def countPrimes(self,n):
        ans = self.get_primes(n)
        print(ans)
