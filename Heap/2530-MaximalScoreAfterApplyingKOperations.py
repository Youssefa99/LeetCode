"""
2530. Maximal Score After Applying K Operations

problem desc:
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
In one operation:
choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

problem difficulty: Medium

Time Complexity: O(NlogN + KlogN)
Space Complexity: O(N)

Constraints:

1 <= nums.length, k <= 105
1 <= nums[i] <= 109

solution intuition: Binary Heap
we store all elements in a priority queue and loop K times with every iteration we get the root of the queue which would be the maximum
value in the list, increment it with our score, remove it from the queue and insert an new element = ceil(nums[i] / 3)
"""
import heapq
import math
class Solution:
    def maxKelements(nums: list[int], k: int) -> int:
        ans = 0
        max_heap = []

        # Add elements one by one into the max-heap
        for num in nums:
            heapq.heappush(max_heap, -num)

        while k > 0:
            k -= 1
            # Retrieve the max element (invert the sign because it's stored as negative)
            max_element = -heapq.heappop(max_heap)
            ans += max_element
            # Add one-third of the max element back to the heap. Rounded up using integer division.
            heapq.heappush(max_heap, -math.ceil(max_element / 3))

        return ans

# Example Test Cases
print(Solution.maxKelements(nums = [10,10,10,10,10], k = 5))
print(Solution.maxKelements(nums = [1,10,3,3,3], k = 3))