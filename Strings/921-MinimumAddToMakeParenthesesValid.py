"""
921. Minimum Add to Make Parentheses Valid

problem desc:
A parentheses string is valid if and only if:
It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

problem difficulty: Medium

Time Complexity: O(N)
Space Complexity: O(1)

Constraints:
1 <= s.length <= 1000
s[i] is either '(' or ')'.

solution intuition: Optimized space Stack
by observing the problem we identify two cases where we need to insert characters in the string
case one: when we find a ")" with no matching opened brackets before it
case two: when we find a "(" whith no matching closed brackets after it
we need to loop over the string tracking both those cases we do that by maintaining two variables unmatched_opened_brackets
and unmatched_closed_brackets 
when we find a "(" we increment the unmatched_opened variable, when we find a ")" we check if we have any unmatched_opened
if we do then we decrement the unmatched_opened if we don't we increment the unmatched_closed. 
the result will be the addition of both variables
"""
class Solution:
    def minAddToMakeValid(s: str) -> int:
        unmatched_opened = 0
        unmatched_closed = 0
        for ch in s:
            if ch == "(":
                unmatched_opened += 1
            else:
                # if we have an unmatched open bracket we match it with the closed bracket we just found
                if unmatched_opened > 0:
                    unmatched_opened -= 1
                else:
                    unmatched_closed += 1
        return unmatched_opened + unmatched_closed

# Example Test Cases
print(Solution.minAddToMakeValid("())"))
print(Solution.minAddToMakeValid("((("))