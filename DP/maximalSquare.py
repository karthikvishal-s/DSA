"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.


Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

"""

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
m=len(matrix)
n=len(matrix[0])
dp=[[0]*(n+1) for _ in range(m+1)]


for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        if matrix[i][j]==0:
            dp[i][j]=0
            continue

        if dp[i][j+1]==1 & dp[i+1][j+1]==1 & dp[i+1][j]==1:
            dp[i][j] = dp[i][j]+1



print(dp)