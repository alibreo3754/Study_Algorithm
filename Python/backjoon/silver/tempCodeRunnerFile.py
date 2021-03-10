import sys

input = sys.stdin.readline

N = int(input())

grape = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]
dp[0] = grape[0]
if N > 1:
    dp[1] = grape[0] + grape[1]
if N > 2:
    dp[2] = grape[2] + max(grape[0], grape[1])
for i in range(3, N):
    dp[i] = grape[i] + max(grape[i - 1] + dp[i - 3], dp[i - 2])
    dp[i] = max(dp[i - 1], dp[i])
print(dp[-1])