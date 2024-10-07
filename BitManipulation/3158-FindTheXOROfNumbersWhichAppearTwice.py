"""
3158. Find the XOR of Numbers Which Appear Twice

problem desc: 
You are given an array nums, where each number in the array appears either once or twice.
Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.

problem difficulty: Easy

Time Complexity: O(N)
Space Complexity: O(N)

Constraints:
1 <= nums.length <= 50
1 <= nums[i] <= 50
Each number in nums appears either once or twice.

solution intuition:
Using frequency map count the occurences of values then the xor of each value that has occurence of 2
"""
class Solution:
    def duplicateNumbersXOR(nums: list[int]) -> int:
        frequency_map = dict()
        for num in nums:
            if num in frequency_map.keys():
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1
        xor = 0
        for i in frequency_map.keys():
            if frequency_map[i] == 2:
                xor ^= i
        return xor

# Example Test cases
print(Solution.duplicateNumbersXOR([1,2,1,3]))
print(Solution.duplicateNumbersXOR([1,2,3]))
print(Solution.duplicateNumbersXOR([1,2,2,1]))