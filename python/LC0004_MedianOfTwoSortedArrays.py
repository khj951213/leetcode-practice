'''
========================================
Leetcode Question 4. Median of Two sorted Arrays
----------------------------------------
Given two sorted arrays `num1` and `num2` of size `m` and `n` respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))
----------------------------------------
Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

Example 2:
    Input nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5
----------------------------------------
Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m+n <= 2000
- 10**6 <= nums1[i], nums2[i] <= 10**6
========================================
'''

# Solution 1: merge sort
def merge_sort(nums1: list[int], nums2: list[int]) -> float:
    nums = sorted(nums1 + nums2)
    length = len(nums)
    mid = length // 2
    if length % 2 == 0:
        return (nums[mid] + nums[mid-1]) / 2
    else:
        return nums[mid]
    
# Solution 2: Binary search partitioning O(log(m+n))
def findMedianSortedArrays(nums1, nums2):
    # Always binary search the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = len(nums1)
    n = len(nums2)

    left = 0
    right = m

    while left <= right:
        # Partition nums1
        partition1 = (left + right) // 2

        # Partition nums2 so total left side has half the elements
        partition2 = (m + n + 1) // 2 - partition1

        # Get values around the partitions
        maxLeft1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float("inf") if partition1 == m else nums1[partition1]

        maxLeft2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float("inf") if partition2 == n else nums2[partition2]

        # Correct partition
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

            # Odd total length
            if (m + n) % 2 == 1:
                return max(maxLeft1, maxLeft2)

            # Even total length
            return (
                max(maxLeft1, maxLeft2)
                + min(minRight1, minRight2)
            ) / 2

        # nums1 partition is too far right
        elif maxLeft1 > minRight2:
            right = partition1 - 1

        # nums1 partition is too far left
        else:
            left = partition1 + 1


def test_cases():
    return [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),

        # One array empty
        ([], [1], 1.0),
        ([], [1, 2], 1.5),
        ([1], [], 1.0),

        # Single values
        ([1], [2], 1.5),
        ([2], [1], 1.5),

        # Duplicates
        ([1, 1], [1, 1], 1.0),
        ([1, 2, 2], [2, 2, 3], 2.0),

        # Negative numbers
        ([-5, -3, -1], [-2], -2.5),
        ([-10, -5], [0, 5, 10], 0.0),

        # Mixed negative and positive
        ([-3, -1], [2, 4], 0.5),
        ([-5, 0, 5], [-2, 2], 0.0),

        # Different sized arrays
        ([1, 2], [3, 4, 5, 6, 7], 4.0),
        ([1], [2, 3, 4, 5, 6], 3.5),

        # Already separated ranges
        ([1, 2, 3], [10, 20, 30], 6.5),

        # Interleaved values
        ([1, 4, 7], [2, 3, 5, 6], 4.0),

        # Larger example
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], 5.5),

        # Zeros
        ([0, 0], [0, 0], 0.0),
        ([0], [0, 1], 0.0),
    ]


def main():
    cases = test_cases()

    for solution in (merge_sort, findMedianSortedArrays):
        print(f"\nTesting {solution.__name__}")

        for case_number, (nums1, nums2, expected) in enumerate(cases, start=1):
            result = solution(nums1, nums2)

            assert result == expected, (
                f"Case {case_number} failed: "
                f"expected {expected}, got {result}"
            )

            print(
                f"Case {case_number}: "
                f"nums1={nums1}, nums2={nums2}, "
                f"expected={expected}, result={result} PASSED"
            )


if __name__ == "__main__":
    main()