## given an array of length N, return sum of all elements


def sum_arr(arr):
    size = len(arr)
    if size == 1 :
        return arr[0]
    print(size,arr,sum_arr(arr[1:]))
    ans  = arr[0]+sum_arr(arr[1:])

def main():
    size = int(input())
    arr = [int(x) for x in input().split()]
    ans = sum_arr(arr)
    print(ans)

if __name__ == '__main__':
    main()