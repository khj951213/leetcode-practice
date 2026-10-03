'''
========================================
Leetcode Question 1. Two Sum
----------------------------------------
You are given an array of integers nums and an integer `target`, 
return indices of the two numbers such that they add up to `target.

You may assume that each input would have excatly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
----------------------------------------
Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0,1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
========================================
'''


# Solution 1: Brute force (unoptimised solution) - Time: O(n**2), Space: O(1)
# Check every element
# Implementation:
def brute_force(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Solution 2: Hashmap - Time: O(n), Space: O(n)
# Check before storing
# Implementation:
def hashmap(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    return []


# Test cases
test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),                        # Basic example
    ([3, 2, 4], 6, [1, 2]),                             # Pair in the middle/end
    ([3, 3], 6, [0, 1]),                                # Duplicate numbers
    ([-3, 4, 3, 90], 0, [0, 2]),                        # Negative and positive
    ([-8, -3, -5, -1], -9, [0, 3]),                     # All negative numbers
    ([0, 4, 3, 0], 0, [0, 3]),                          # Two zeros
    ([5, 0, 2, 8], 8, [1, 3]),                          # Zero and a positive number
    ([1, 2, 3, 4, 9], 10, [0, 4]),                      # First and last elements
    ([3, 2, 4], 6, [1, 2]),                             # Cannot reuse the first 3
    ([1_000_000_000, -1_000_000_000, 5], 0, [0, 1]),    # Large numbers
]

for solution in (brute_force, hashmap):
    for case_number, (nums, target, expected) in enumerate(test_cases, start=1):
        result = solution(nums, target)

        # Either index order is valid.
        assert sorted(result) == sorted(expected), (
            f"{solution.__name__}: case {case_number} failed. "
            f"Expected {expected}, got {result}"
        )

    print(f"{solution.__name__}: all 10 tests passed!")