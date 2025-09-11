"""
                Longest Palindromic Subsequence
"""

s1="abgcba"   # o/p = "abcba" or "abgcba"

s2=s1[::-1]
m,n=len(s1),len(s2)

dp=[[0]*(n+1) for _ in range(m+1)]

res=""
for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
            res=res+s1[i-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])



    

print(dp[m][n])
print(res)

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