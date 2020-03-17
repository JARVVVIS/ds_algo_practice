## Find sum of all multiples of 3 and 5 below 1000

def get_sum(num):
    ans=0
    for val in range(3,num):
        if not val%3 or not val%5:
            ans+=val
    return ans


def main():
    num = int(input())
    ans = get_sum(num)
    print(ans)



if __name__ == '__main__':
    main()