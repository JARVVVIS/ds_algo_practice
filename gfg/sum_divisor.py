# Given a natural number n, the task is to find sum of divisors of all the divisors of n.


def find_sum(val):
    ans=0
    for num in range(1,val+1):
        if not val%num:
            ans+=num
    return ans

def main():
    t = int(input())
    for _ in range(t):
        num = int(input())
        ans = 0
        for val in range(1,num+1):
            if not num%val:
                ans+=find_sum(val)
        print(ans)

if __name__ == '__main__':
    main()
