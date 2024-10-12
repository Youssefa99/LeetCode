"""
2406. Divide Intervals Into Minimum Number of Groups

problem desc:
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].
You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.
Return the minimum number of groups you need to make.
Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

problem difficulty: Medium

Time Complexity: O(NlogN)
Space Complexity: O(N)

Constraints:
1 <= intervals.length <= 10^5
intervals[i].length == 2
1 <= lefti <= righti <= 10^6

solution intuition: Line Sweep Algorithm
"""
class Solution:
    def minGroups(intervals: list[list[int]]) -> int:
        # Convert the intervals to two events
        # start as (start, 1) and end as (end + 1, -1)
        events = []

        for interval in intervals:
            events.append((interval[0], 1))  # Start event
            events.append((interval[1] + 1, -1))  # End event (interval[1] + 1)

        # Sort the events first by time, and then by type (1 for start, -1 for end).
        events.sort(key=lambda x: (x[0], x[1]))
        concurrent_intervals = 0
        max_concurrent_intervals = 0

        # Sweep through the events
        for event in events:
            concurrent_intervals += event[1]  # Track currently active intervals
            max_concurrent_intervals = max(
                max_concurrent_intervals, concurrent_intervals
            )  # Update max

        return max_concurrent_intervals

print(Solution.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))
print(Solution.minGroups([[1,3],[5,6],[8,10],[11,13]]))