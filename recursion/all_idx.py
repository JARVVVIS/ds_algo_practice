## ALL index of x in an array , -1 if not present

def all_idx(arr,x,idx_list):
    if x == arr[-1]:
        idx_list.append(len(arr)-1)
    if len(arr)==1:
        return -1
    all_idx(arr[:-1],x,idx_list)
    return idx_list


def main():
    n   =  int(input())
    arr =  [int(x) for x in input().split()]
    x   = int(input())
    idx_list = []
    ans = all_idx(arr,x,idx_list)
    for idx in reversed(ans):
        print(idx,end=' ')


if __name__ == '__main__':
    main()