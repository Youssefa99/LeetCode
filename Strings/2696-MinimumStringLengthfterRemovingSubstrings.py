"""
2696. Minimum String Length After Removing Substrings

problem desc:
You are given a string s consisting only of uppercase English letters.
You can apply some operations to this string where, in one operation, you can remove any occurrence of one of the substrings "AB" or "CD" from s.
Return the minimum possible length of the resulting string that you can obtain.
Note that the string concatenates after removing the substring and could produce new "AB" or "CD" substrings.

problem difficulty: Easy

Time Complexity: O(N.d)
Space Complexity: O(1)

Constraints:
1 <= s.length <= 100
s consists only of uppercase English letters.

solution intuition: 
loop through the string removing any instances you find through of AB or CD, to handle the problem of new patterns forming after removing
old patterns we keep looping until no instances of AB or CD exists we chekck for that by comparing string length before and after looping
if they are equal that means we no longer have instances of substrings in the string which adds to the complexity of our code d
"""
class Solution:
    def minLength(s: str) -> int:
        substrings = set(["AB", "CD"])
        old_len = len(s)
        for substring in substrings:
            s = s.replace(substring, '')
        new_len = len(s)
        # check if we removed anything from the string and keep looping until we no longer remove anything from it
        while new_len != old_len:
            old_len = new_len
            for substring in substrings:
                s = s.replace(substring, '')
            new_len = len(s)
        return len(s)

# Example Test cases
print(Solution.minLength("ABFCACDB"))
print(Solution.minLength("ACBBD"))