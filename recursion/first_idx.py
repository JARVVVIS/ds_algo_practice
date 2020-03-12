## return first index of x in an array, return -1 if x is not present in array


def first_idx(arr,x,n):
    if x == arr[0]:
        return n - len(arr)
    if len(arr)==1:
        return -1
    return first_idx(arr[1:],x,n)

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    x = int(input())
    idx = first_idx(arr,x,n)
    print(idx)


if __name__ == '__main__':
    main()