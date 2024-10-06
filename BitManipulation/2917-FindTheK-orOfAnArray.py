"""
2917. Find the K-or of an Array

problem desc: 
You are given an integer array nums, and an integer k. Let's introduce K-or operation by extending the standard bitwise OR. In K-or, 
a bit position in the result is set to 1 if at least k numbers in nums have a 1 in that position. Return the K-or of nums.

problem difficulty: easy

Time Complexity: O(N)
Space Complexity: O(1)

Constraints:
1 <= nums.length <= 50
0 <= nums[i] < 231
1 <= k <= nums.length

solution intuition:
initialize an array of size 32 with initial value of 0, loop through each number checking which bits are set and increment it's 
value in the array. then loop through each element in the array checking if occurrence[i] >= k if true then ans += 2^i
"""
class Solution:
    def findKOr(nums: list[int], k: int) -> int:
        # frequency array for set bits
        k_array = [0]*32
        for num in nums:
            for i in range(32):
                # check if bit is set
                if num & (1 << i) != 0:
                    k_array[i] += 1
        ans = 0
        for i in range(32):
            if k_array[i] >= k:
                ans += pow(2,i)
        return ans
    
# Example Test Cases
print(Solution.findKOr([7,12,9,8,9,15], 4))
print(Solution.findKOr([2,12,1,11,4,5], 6))
print(Solution.findKOr([10,8,5,9,11,6,8], 1))