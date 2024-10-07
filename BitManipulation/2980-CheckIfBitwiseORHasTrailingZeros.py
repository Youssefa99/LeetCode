"""
2980. Check if Bitwise OR Has Trailing Zeros

problem desc: 
You are given an array of positive integers nums.
You have to check if it is possible to select two or more elements in the array such that the bitwise OR of the selected elements has at least one trailing zero in its binary representation.
For example, the binary representation of 5, which is "101", does not have any trailing zeros, whereas the binary representation of 4, which is "100", has two trailing zeros.
Return true if it is possible to select two or more elements whose bitwise OR has trailing zeros, return false otherwise.

problem difficulty: Easy

Time Complexity: O(N)
Space Complexity: O(1)

Constraints:
2 <= nums.length <= 100
1 <= nums[i] <= 100

solution intuition:
since the only way for the bitwise OR of two elements to have trailing zeroes is for both elements to be even the problem becomes
checking whether an array has atleast two even elements in it
"""
class Solution:
    def hasTrailingZeros(nums: list[int]) -> bool:
        even = False
        for num in nums:
            if num % 2 == 0:
                if even:
                    return True
                else:
                    even = True
        return False

# Example Test Cases
print(Solution.hasTrailingZeros([1,2,3,4,5]))
print(Solution.hasTrailingZeros([2,4,8,16]))
print(Solution.hasTrailingZeros([1,3,5,7,9]))