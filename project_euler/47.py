# Find first four consecutive integers to have 4 distinct prime factors each
import math

def get_primes(unique,num):
    factors = [0]*(num+1)
    for val in range(2,num+1):
        og = val
        temp=0
        last_f = 0
        while not val%2:
            val=val//2
            temp=1
        sqrt = int(math.sqrt(val))
        for f in range(3,sqrt+1,2):
            while not val%f:
                val=val//f 
                if last_f!=f:
                    temp+=1
                    last_f = f
        if val>2:
            temp+=1
        if temp==unique:
            factors[og] = 1
    return factors



def main():
    num = int(input())
    MAX = int(1e6) ## Max operations
    distinct_list = get_primes(num,MAX)
    print('Done')
    for val in range(len(distinct_list)-4):
        a,b,c,d = distinct_list[val],distinct_list[val+1],distinct_list[val+2],distinct_list[val+3]
        if a and b and c and d:
            print(val)
            break







if __name__ == '__main__':
    main()