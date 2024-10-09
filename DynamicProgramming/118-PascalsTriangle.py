"""
118. Pascal's Triangle

problem desc:
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it

problem difficulty: Easy

Time Complexity: O(N^2)
space Complexity: O(N^2)

Constraints:
1 <= numRows <= 30

solution intuition: Dynamic Programming
Utilizing the recurrence relation of middle element values in pascal's triangle where a middle element value is
nCr = n-1Cr + n-1Cr-1 while maintaining that values on the edges of each row is always one
"""
class Solution:
    def generate(numRows: int) -> list[list[int]]:
        dp = [[1], [1, 1]] 
        if numRows == 1:
            return [dp[numRows - 1]]
        elif numRows == 2:
            return dp
        i = 2
        row = 0
        while i < numRows:
            current = []
            while row <= i:
                if row == 0 or row == i:
                    current.append(1)
                else:
                    current.append(dp[i-1][row] + dp[i-1][row-1])
                row += 1
            dp.append(current)
            i += 1
            row = 0
        return dp

# Example Test Cases
print(Solution.generate(5))
print(Solution.generate(1))