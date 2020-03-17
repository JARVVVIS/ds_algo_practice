import math

## O(n)
def get_primes(num):
    lp = [0]*(num+1)
    primes = []
    for val in range(2,num+1):
        if not lp[val]:
            lp[val] = val 
            primes.append(val)
        j=0
        while j<len(primes) and primes[j]*val<=num and primes[j]<=lp[val]:
            lp[primes[j]*val] = primes[j]
            j+=1
    return lp,primes


def get_div(num,lp):
    ans = {}
    while num!=1:
        lpf = lp[num] ## least prime factor of this number
        num = num//lpf
        if lpf not in ans.keys():
            ans[lpf] = 0
        ans[lpf] += 1
    val = 1
    for factor in ans:
        val *= (ans[factor]+1)
    return val


def get_sum(num,lp):
    ans = [0]*(num+1)
    ans[1] = 1
    for val in range(2,num+1):
        ans[val] = get_div(val,lp)+ans[val-1]
    return ans



def main():
    MAX = int(1e5)
    lp,primes = get_primes(MAX)
    div_list  = get_sum(MAX,lp)

    t = int(input())
    for _ in range(t):
        num = int(input())
        print(div_list[num])



if __name__ == '__main__':
    main()