"""
2932. Maximum Strong Pair XOR I

problem desc: 
You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:
|x - y| <= min(x, y)
You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.
Return the maximum XOR value out of all possible strong pairs in the array nums.
Note that you can pick the same integer twice to form a pair.

problem difficulty: Easy

Time Comlexity: O(N^2)
Space Complexity: O(1)

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 100

solution intuition:
Brute Force approach - use nested loops to iterate over elements comparing whether they are strong pairs, if they are check their 
XOR value 
"""

class Solution:
    def maximumStrongPairXor(nums: list[int]) -> int:
        maximum = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    maximum = max(maximum, nums[i]^nums[j])
        return maximum

# Example Test Cases
print(Solution.maximumStrongPairXor([1,2,3,4,5]))
print(Solution.maximumStrongPairXor([10,100]))
print(Solution.maximumStrongPairXor([5,6,25,30]))