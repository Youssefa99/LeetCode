"""
3226. Number of Bit Changes to Make Two Integers Equal

problem desc: 
You are given two positive integers n and k.
You can choose any bit in the binary representation of n that is equal to 1 and change it to 0.
Return the number of changes needed to make n equal to k. If it is impossible, return -1.

Time complexity: O(1)
Space Complexity: O(1)

Constraints:
1 <= n, k <= 10^6

solution intuition:
assume x = n ^ k, all set bits in x denotes the different bit values in n and k ie: if x[i] = 1 that means that n[i] != k[i]
now all that is missing is checking whether n[i] = 1 if true then we can change that bit to zero if not then both return -1
note: since the constraint specifies maximum value of k is 10^6 and binary representation of it is 11110100001001000000 that
means that we only need to perform twenty one iteration
"""
class Solution:
    def minChanges(n: int, k: int) -> int:
        if n == k:
            return 0
        # get the positions where bits are different
        xor = n ^ k
        changes = 0
        for i in range(21):
            if xor & (1 << i) != 0:
                # check if the bit in N is set
                if n & (1 << i) != 0:
                    changes += 1
                else:
                    return -1
        return changes

# Example Test cases:
print(Solution.minChanges(13, 4))
print(Solution.minChanges(21, 21))
print(Solution.minChanges(14, 13))