'''
========================================
Leetcode Question 3. Longest substring without repeating characters
----------------------------------------
Given a string `s`, find the length of the longest substring without duplicate characters.

----------------------------------------
Example 1:
    Input: s = 'abcabcbb'
    Output: 3
    Explanation: The answer is 'abc' with the length of 3.
                Note that 'bca' and 'cab' are also correct

Example 2:
    Input: s = 'bbbbb'
    Output: 1
    Explanation: The answer is 'b', with the length of 1.
    
----------------------------------------
Constraints:
-  0 <= s.length <= 10**6
- `s` consists of English letters, digits, symbols and spaces.
========================================
'''
# Solution: brute force
def brute_force(s: str) -> int:
    max_len = 0

    for i in range(len(s)):
        seen = set()

        for j in range(i, len(s)):
            if s[j] in seen:
                break

            seen.add(s[j])

            length = j - i + 1
            max_len = max(max_len, length)

    return max_len


# Solution: Dictionary storing last index
def two_pointers(s: str) -> int:
    last_seen = {}
    left = 0
    max_len = 0

    for right, c in enumerate(s):
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1

        last_seen[c] = right

        length = right - left + 1
        max_len = max (max_len, length)

    return max_len


# Solution: sliding window (set + two pointers)
def sliding_window(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for idx, c  in enumerate(s):

        # seen always contains exactly the characters between `left` and `idx`
        while c in seen:
            seen.remove(c)
            left += 1 

        seen.add(c)

        length = idx - left + 1
        max_len = max(length, max_len)

    return max_len

def test_cases():
    return [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("a", 1),
        ("au", 2),
        ("dvdf", 3),
        ("abba", 2),
        ("abcdef", 6),
        ("tmmzuxt", 5),
    ]


def main():
    cases = test_cases()

    for case_number, (s, expected) in enumerate(cases, start=1):
        result = brute_force(s)

        assert result == expected, (
            f"Case {case_number} failed: "
            f"input={s!r}, "
            f"expected={expected}, "
            f"got={result}"
        )

        print(
            f"Case {case_number}: "
            f"input={s!r}, "
            f"expected={expected}, "
            f"result={result} PASSED"
        )


if __name__ == "__main__":
    main()