# The Tribonacci sequence Tn is defined as follows: 

# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

# Given n, return the value of Tn.


def trib(num,vals):
    if num in vals.keys():
        return vals[num]
    else:
        m = num-3
        ans = trib(m,vals)+trib(m+1,vals)+trib(m+2,vals)
        vals[num] = ans
        return ans 

def main():
    num = int(input()) ## input the nth tribonacci number to be found
    vals = {0:0,1:1,2:1}
    ans = trib(num,vals)
    print(ans)


if __name__ == '__main__':
    main()
