"""
                    Longest Common Subsequence  
"""

s1="aggtab"
s2="gxtxayb"

# First considering the counting of all elements and keeping track of it...So we prefer DP
# Under DP ,we prefer tabulation  Memoization uses recursion stack → risk of stack overflow for large inputs (e.g., strings of length 10^3 or 10^4).

m=len(s1)
n=len(s2)

dp=[[0]*(n+1) for _ in range(m+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[m][n])

print(dp)


# I constructed this backtracking on my own 🔥

def backtrack(s1,s2,dp,m,n):
    res=""
    i,j=m,n
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            res=s1[i-1]+res
            i-=1
            j-=1
        else:
            if dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1
    return res

print(backtrack(s1,s2,dp,m,n))


