"""
1497. Check If Array Pairs Are Divisible by k

problem desc:
Given an array of integers arr of even length n and an integer k.
We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.
Return true If you can find a way to do that or false otherwise.

problem difficulty: Medium

Time Complexity: O(N)
Space Complexity: O(K)

Constraints:
arr.length == n
1 <= n <= 10^5
n is even.
-10^9 <= arr[i] <= 10^9
1 <= k <= 10^5

solution intuition: Counting modulo K
looping on each element we get the modulo value that is needed to exist in the array that when it's added to this element we get a pair
that is divisible by k. this is calculated as (i % k + k) % k where we add a further K and get the remainder again to account for
negative values. we count the occurrence of these values and if for each element i%k there exists an equal number of element j
where j%k = k - i%k 
"""
class Solution:
    def canArrange(arr: list[int], k: int) -> bool:
        modulo_count = dict()
        # count the remainder of each element
        for i in arr:
            modulo_count[(i % k + k) % k] = (
                modulo_count.get((i % k + k) % k, 0) + 1
            )
        # loop through the array and check that for each element there exists equivalent element j 
        for i in arr:
            rem = (i % k + k) % k
            # Base Case: if rem is zero we need to check that there are even numbers of elements i where i%k = 0
            if rem == 0:
                if modulo_count[rem] % 2 != 0:
                    return False
            elif modulo_count[rem] != modulo_count.get(k - rem, 0):
                return False
        return True
    
# Example Test Cases
print(Solution.canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5))
print(Solution.canArrange(arr = [1,2,3,4,5,6], k = 7))
print(Solution.canArrange(arr = [1,2,3,4,5,6], k = 10))