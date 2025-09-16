"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 
"""
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
n=len(triangle)


dp=[[0]*len(row) for row in triangle]
dp[0][0] = triangle[0][0]

for i in range(1,n):
    for j in range(len(triangle[i])):
        if j==0:
            dp[i][j]=dp[i-1][j]+triangle[i][j]
        elif j==i:
            dp[i][j] = dp[i-1][j-1]+triangle[i][j]
        else:
            dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
    

print(min(dp[n-1]))