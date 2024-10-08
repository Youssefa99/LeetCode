"""
1963. Minimum Number of Swaps to Make the String Balanced

problem desc:
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets
'[' and n / 2 closing brackets ']'.
A string is called balanced if and only if:
It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.
Return the minimum number of swaps to make s balanced.

problem difficulty: Medium

Time Complexity: O(N)
Space Complexity: O(1)

Constraints:
n == s.length
2 <= n <= 106
n is even.
s[i] is either '[' or ']'.
The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.

solution intuition:
we need to determine a criteria upon which we decide whether we need to perform a swap or not. one way we can decide whether a swap 
is needed or not is through deciding whether an opening bracket "[" is an unmatched opening bracket or not
an unmatched opening bracket is an opening bracket that we encounter without later encountering an equivalent closing bracket
by counting the number of unmatched opening brackets we can determine the number of swaps needed where
minimum number of swaps = unmatched_opening_bracket + 1 / 2
"""
class Solution:
    def minSwaps(s: str) -> int:
        unmatched_opening_brackets = 0
        for c in s:
            if c == "[":
                unmatched_opening_brackets += 1
            else:
                if unmatched_opening_brackets > 0:
                    unmatched_opening_brackets -= 1
        return (unmatched_opening_brackets + 1)//2

# Example Test Cases
print(Solution.minSwaps("][]["))
print(Solution.minSwaps("]]][[["))
print(Solution.minSwaps("[]"))