"""
1593. Split a String Into the Max Number of Unique Substrings

problem desc:
Given a string s, return the maximum number of unique substrings that the given string can be split into.
You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
A substring is a contiguous sequence of characters within a string.

problem difficulty: Medium

Time Complexity: O(N.2^N)
Space Complexity: O(1)

Constraints:
1 <= s.length <= 16
s contains only lower case English letters.

solution intuition:
use backtracking to get all substrings while storing them in a set to prevent duplicates
"""
class Solution:
    def backtrack(s, start, seen):
        if start == len(s):
            return 0

        max_count = 0

        for end in range(start + 1, len(s) + 1):
            sub_string = s[start:end]
            if sub_string not in seen:
                seen.add(sub_string)
                max_count = max(max_count, 1 + Solution.backtrack(s, end, seen))
                seen.remove(sub_string)

        return max_count
    
    def maxUniqueSplit(s: str) -> int:
        seen = set()
        return Solution.backtrack(s, 0, seen)

# Example Test Cases
print(Solution.maxUniqueSplit(s = "ababccc"))
print(Solution.maxUniqueSplit(s = "aba"))
print(Solution.maxUniqueSplit(s = "aa"))