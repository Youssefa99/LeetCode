"""
1980. Find Unique Binary String

problem desc:
Given an array of strings nums containing n unique binary strings each of length n, 
return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them

problem difficulty: medium

Time Complexity: O(N)
Space Complexity: O(1)

Constraints:
n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.

solution intuition: Cantor's diagonal argument
applying cantor's diagonal argument we can get the binary number that does not appear in the list
"""
class Solution:
    def findDifferentBinaryString(nums: list[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")
        return "".join(ans)

# Example Test cases:
print(Solution.findDifferentBinaryString(["01","10"]))
print(Solution.findDifferentBinaryString(["00","01"]))
print(Solution.findDifferentBinaryString(["111","011","001"]))
    