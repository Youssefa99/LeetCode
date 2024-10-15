"""
2938. Separate Black and White Balls

problem desc:

There are n balls on a table, each ball has a color black or white.
You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.
In each step, you can choose two adjacent balls and swap them.
Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.

problem difficulty: Medium

Time Complexity: O(N)
Space Complexity: O(1)

Constraints:
1 <= n == s.length <= 10^5
s[i] is either '0' or '1'.

solution intuition:
loop through the array at each one we encounter we calculate the difference between it's current position and the position it should 
be in where expected position = string_size - total_ones + current_one, the minimum swaps would be the summation of that process 
"""
class Solution:
    def minimumSteps(s: str) -> int:
        count1s = 0
        # calculate total number of 1s
        for ch in s:
            if ch == "1":
                count1s += 1
        # refers to the order of the current one of all the ones in the string
        current = 0
        swaps = 0
        for i in range(len(s)):
            if s[i] == "1":
                expected = len(s) - count1s + current
                swaps += abs(expected - i)
                current += 1
        return swaps
    
# Example Test Cases
print(Solution.minimumSteps("101"))
print(Solution.minimumSteps("100"))
print(Solution.minimumSteps("0111"))