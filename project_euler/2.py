## Sum of all even-valued fibonacci terms below 4 million

def get_sum(num):
    ans=2
    val=0
    a=1
    b=2
    while val<num:
        val=a+b 
        a=b 
        b=val 
        if not val%2:
            print(val)
            ans+=val
    return ans


def main():
    MAX = int(input()) ## Max Range
    ans = get_sum(MAX)
    print(ans)

if __name__ == '__main__':
    main()