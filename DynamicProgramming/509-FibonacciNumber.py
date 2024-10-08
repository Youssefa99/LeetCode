"""
509. Fibonacci Number

problem desc:
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

problem difficulty: Easy

Time Complexity: O(N)
Space Complexity: O(N)

Constraints:
0 <= n <= 30

solution intuition: Dynamic programming
"""
class Solution:
    def fib(n: int) -> int:
        fib = [0, 1]
        if n < 2:
            return fib[n]
        for i in range(2,n+1):
            fib.append(fib[i-1]+fib[i-2])
        return fib[n]

# Example Test Cases
print(Solution.fib(2))
print(Solution.fib(3))
print(Solution.fib(4))
