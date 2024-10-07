"""
3095. Shortest Subarray With OR at Least K I

problem desc:
You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

Time Complexity: O(N^2)
Space Complexity: O(1)

Constraints:
1 <= nums.length <= 50
0 <= nums[i] <= 50
0 <= k < 64

solution intuition:
using Brute Force Approach
"""

class Solution:
    def minimumSubarrayLength(nums: list[int], k: int) -> int:
        n = len(nums)
        # this will be used to keep track of the minimum subarray length found.
        min_len = n + 1
        curORVal = 0
        for i in range(n):
            curORVal = 0
            for j in range(i, n):
                curORVal |= nums[j]
                if curORVal >= k:
                    min_len = min(min_len, j+1-i)
        # if `minLen` is still equal to `n + 1`, no valid subarray was found, so return -1.
        # otherwise, return the minimum length of the special subarray found.            
        return min_len if min_len != n + 1 else -1

# Example Test cases:
print(Solution.minimumSubarrayLength([1,2,3], 2))
print(Solution.minimumSubarrayLength([2,1,8], 10))
print(Solution.minimumSubarrayLength([1,2], 0))