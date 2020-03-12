## Find number of digits in a number

def count_dig(num):
    if num==0:
        return 0
    ans = 1+count_dig(num//10)
    return ans

def main():
    num =  int(input()) ## input the number
    ans = count_dig(num)
    print(ans)

if __name__ == '__main__':
    main()