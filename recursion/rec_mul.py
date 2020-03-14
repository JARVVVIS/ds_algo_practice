## given two integers m and n return their multiplication using recurssion

def mul(m,n):
    if n==0 or m==0: 
        return 0
    if n==1:
        return m
    return m+mul(m,n-1)



def main():
    m = int(input())
    n = int(input())
    ans = mul(abs(m),abs(n))
    sign = 1
    if m<0 and n<0:
        pass
    elif m<0 or n<0:
        sign = -1
    ans*=sign
    print(ans)

if __name__ == '__main__':
    main()