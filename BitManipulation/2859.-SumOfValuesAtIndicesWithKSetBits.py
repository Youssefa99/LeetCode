"""
2859. Sum of Values at Indices With K Set Bits

problem desc:
You are given a 0-indexed integer array nums and an integer k.
Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.
The set bits in an integer are the 1's present when it is written in binary.

problem difficulty: Easy

Time Complexity: O(NlogN)
Space Complexity: O(1)

Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 10^5
0 <= k <= 10

solution intuition:
loop through every element in array checking if number of set bits = k, check for set bits using Brian Kernighan Algorithm
"""

class Solution:
    def sumIndicesWithKSetBits(nums: list[int], k: int) -> int:
        # count number of bits using brian kernighan algorithm
        def countSetBits(num: int) -> int:
            count = 0
            while num:
                num = num & (num - 1)
                count += 1
            return count
        n = len(nums)
        ans = 0
        for i in range(n):
            if countSetBits(i) == k:
                ans += nums[i]
        return ans

# Example Test Cases
print(Solution.sumIndicesWithKSetBits([5,10,1,5,2], 1))
print(Solution.sumIndicesWithKSetBits([4,3,2,1], 2))
