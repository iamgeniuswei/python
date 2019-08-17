def MaxChildArrayOrder(a):
    n = len(a)
    tmp = []
    for i in range(0, n):
        tmp.append(i)
    for i in range(1,n):
        for j in range(0,i):
            if a[i] > a[j] and tmp[j]+1 > tmp[i]:
                tmp[i] = tmp[j]+1


    max = tmp[0]
    for i in range(1,n):
        if tmp[i] > max:
            max = tmp[i]

    return max

import numpy as np

def sum(arr=None, n=None, m=None):
    dp = np.zeros((20, 20))
    dp[0][0] =1
    for j in range(1, m+1):
        dp[0][j] = 0
    for i in range(1, n+1):
        dp[i][0] = 1
        for j in range(0, m+1):
            cur_arr = arr[i-1]
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    print('ok')
    print(dp[n][m])

def lcs(str1, str2):
    try:
        n_str1 = len(str1)
        n_str2 = len(str2)
        dp = np.zeros((n_str1 + 1, n_str2 + 1), dtype=np.int)
        for i in range(1, n_str1 + 1):
            for j in range(1, n_str2 + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(dp[n_str1][n_str2])
    except Exception as e:
        print(str(e))



# a = [3,1,4,1,5,9,2,6,5]
# max = MaxChildArrayOrder(a)
# print(max)

# sum([5,5,10,2,3],5,15)
lcs("FOSH", "FISH")