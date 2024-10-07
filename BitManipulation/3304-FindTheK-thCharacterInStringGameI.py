"""
3304. Find the K-th Character in String Game I

problem desc:
Alice and Bob are playing a game. Initially, Alice has a string word = "a".
You are given a positive integer k.
Now Bob will ask Alice to perform the following operation forever:
Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.
Note that the character 'z' can be changed to 'a' in the operation.

problem difficulty: Easy

Time Complexity: O(1)
Space Complexity: O(1)

Constraints:
1 <= k <= 500

solution intuition:
by observing that the character k-1 in the sequence is related to the number of set bits in the binary k-1 representation 
ie char[k-1] = a + numberOf1s(k-1)
"""
class Solution:
    def kthCharacter(k: int) -> str:
        # get number of set bits in the binary representation of (k - 1)
        flips = bin(k-1).count('1')
        return chr(ord('a') + flips)

# Example Test cases
print(Solution.kthCharacter(5))
print(Solution.kthCharacter(10))