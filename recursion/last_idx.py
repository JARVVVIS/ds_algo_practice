## Last index of x in an array , -1 if not present

def last_idx(arr,x,n):
    if x == arr[-1]:
        return len(arr)-1
    if len(arr)==1:
        return -1
    return last_idx(arr[:-1],x,n)


def main():
    n   =  int(input())
    arr =  [int(x) for x in input().split()]
    x   = int(input())
    ans = last_idx(arr,x,n)
    print(ans)


if __name__ == '__main__':
    main()