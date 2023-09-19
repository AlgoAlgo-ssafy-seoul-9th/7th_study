# 9527_1의개수세기_howmanyone
# 시간초과
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

dp = [0]*(len(bin(10**16))-1)
dp[1] = 1
for i in range(2, 55):
    dp[i] = 2**(i-1) + 2*dp[i-1]

bA = len(bin(A))-2
bB = len(bin(B))-2
temp = 0
for i in range(2**(bB-1), B+1):
    # print(bin(i))
    temp += bin(i).count('1')
temp2 = 0
for i in range(A, 2**(bA-1)):
    # print(bin(i))
    temp2 += bin(i).count('1')
print(dp[bB-1] - dp[bA-1] + temp + temp2)

