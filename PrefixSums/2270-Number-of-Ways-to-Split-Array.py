"""
2270. Number of Ways to Split Array

problem desc:
You are given a 0-indexed integer array nums of length n.
nums contains a valid split at index i if the following are true:
The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.

Time Complexity: O(N)
space Complexity: O(N)

Constraints:
2 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5

solution intuition:
by creating a suffix array to calculate the total sum from the right all the way to the current index i+1 while maintaing a prefix array to
calculate the total sum from the left all the way to the current index i. we compare both sums if they satisfy the condition then we increment the 
valid number of splits .
"""
class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        right_sum = [0] * len(nums)
        curr_sum = 0
        splits = 0
        left_sum = 0 
        for i in range(len(nums)-1, -1, -1):
            curr_sum += nums[i]
            right_sum[i] = curr_sum
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            if left_sum >= right_sum[i+1]:
                splits += 1
        return splits

# Example Test Cases
print(Solution.waysToSplitArray(nums = [10,4,-8,7]))
print(Solution.waysToSplitArray([2,3,1,0]))
