# Write a program to find x to the power n (i.e. x^n). 
# Take x and n from the user. You need to return the answer.

def power(x=1,n=1):
    if x==1:
        return 1
    if n==1:
        return x
    if n<=0 :
        return 1
    return x*power(x,n-1)



def main():
    x,n = [int(x) for x in input().split()]
    ans = power(x,n)
    print(ans)

if __name__ == '__main__':
    main()