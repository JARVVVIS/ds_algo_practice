# Take as input a number n. Determine whether it is prime or not. If it is prime, 
# print "Prime" otherwise print "Not Prime".


def main():
    x = int(input()) 
    ans = 'Prime'
    for num in range(2,x):
        if x%num==0:
            ans='Not Prime'
            break
    print(ans)


if __name__ == '__main__':
    main()