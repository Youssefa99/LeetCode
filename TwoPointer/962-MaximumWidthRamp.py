"""
962. Maximum Width Ramp

problem desc:
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

problem difficulty: Medium

Time Complexity: O(N)
Space Complexity: O(N)

Constraints:

2 <= nums.length <= 5 * 104
0 <= nums[i] <= 5 * 104

solution intuition: Two Pointers + maxArray
We can notice that it would be helpful to know the maximum value from each index to the end of the array. 
Given this information, we can easily check if the ramp condition is satisfied for any left index while iterating from the 
start of the array. Thus, we initialize rightMax where each element at index i stores the maximum value from index i to the last index.
We populate this array in reverse order. Starting from the end of the nums array, 
we set the last element of rightMax to be equal to the last element of nums. For all previous indices, 
we store the maximum of the current value in nums[i] and the value at rightMax[i + 1]. 
This ensures that each index in rightMax contains the highest value from that index to the end of the original array.
"""
class Solution:
    def maxWidthRamp(nums: list[int]) -> int:
        n = len(nums)
        right_max = [None] * n

        # Fill right_max array with the maximum values from the right
        right_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        left = 0
        right = 0
        max_width = 0

        # Traverse the array using left and right pointers
        while right < n:
            # Move left pointer forward if current left exceeds right_max
            while left < right and nums[left] > right_max[right]:
                left += 1
            max_width = max(max_width, right - left)
            right += 1

        return max_width

# Example Test cases
print(Solution.maxWidthRamp([6,0,8,2,1,5]))
print(Solution.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))