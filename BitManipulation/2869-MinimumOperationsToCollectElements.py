"""
2869. Minimum Operations to Collect Elements

problem desc: 
You are given an array nums of positive integers and an integer k.
In one operation, you can remove the last element of the array and add it to your collection.
Return the minimum number of operations needed to collect elements 1, 2, ..., k.

problem difficulty: Easy

Time Complexity: O(N)
Space Complexity: O(1)

solution intuition: 
the go to solution would be using a frequency map to check for the occurrences of values within the range 1,2,..k
and getting the earliest occurrence of all numbers within that range say i then return len(nums) - i
this would give us both time and space complexity of O(N), to optimize space instead of using a frequency map we use binary value
where each 1 in that number denotes that we have already found that number before when all bits in range 0->k-1 are set in that number
then we have found all the occurrences of the sequence 
"""

class Solution:
    def minOperations(nums: list[int], k: int) -> int:
        flag = 0  # Use this variable to mark numbers
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= k:
                flag |= 1 << (nums[i] - 1)  # Mark if the number is less than or equal to the required k
            if flag == (1 << k) - 1:  # If all numbers from 1 to k are marked
                return len(nums) - i
        return -1
    
# Example Test Cases
print(Solution.minOperations([3,1,5,4,2], 2))
print(Solution.minOperations([3,1,5,4,2], 5))
print(Solution.minOperations([3,2,5,3,1], 3))