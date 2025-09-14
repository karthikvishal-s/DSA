n=7
m=3


dp=[[0]*(n) for _ in range(m)]

for i in range(1,m):
    dp[i][0]=1
for i in range(1,n):
    dp[0][i]=1


for i in range(1,m):
    for j in range(1,n):

        dp[i][j]=dp[i][j-1]+dp[i-1][j]

print(dp[m-1][n-1])