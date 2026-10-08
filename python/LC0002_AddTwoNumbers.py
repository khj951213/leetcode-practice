'''
========================================
Leetcode Question 2. Add two numbers
----------------------------------------
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
----------------------------------------
Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
========================================
'''

class ListNode:
    def __init__(self, val:int = 0, next: ListNode = None):
        self.val = val
        self.next = next


# Solution
def add_two_numbers(l1: ListNode, l2: ListNode):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 is not None or l2 is not None or carry > 0:
        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0

        total = val1 + val2 + carry
        digit = total % 10
        carry = total // 10

        current.next = ListNode(digit)
        current = current.next

        if l1 is not None:
            l1 = l1.next

        if l2 is not None:
            l2 = l2.next

    return dummy.next

# Test cases
def to_linked_list(digits: list[int]) -> ListNode:
    dummy = ListNode()
    current = dummy

    for digit in digits:
        current.next = ListNode(digit)
        current = current.next

    return dummy.next


def to_list(node: ListNode) -> list[int]:
    digits = []

    while node is not None:
        digits.append(node.val)
        node = node.next

    return digits

def test_cases():
    return [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),       # 342 + 465 = 807
        ([0], [0], [0]),                         # 0 + 0 = 0
        ([0], [3, 2, 1], [3, 2, 1]),             # 0 + 123 = 123
        ([2], [3], [5]),                         # 2 + 3 = 5
        ([5], [5], [0, 1]),                      # 5 + 5 = 10
        ([9, 9, 9], [1], [0, 0, 0, 1]),          # 999 + 1 = 1000
        ([1], [9, 9], [0, 0, 1]),                # 1 + 99 = 100
        ([1, 2], [3, 4, 5], [4, 6, 5]),          # 21 + 543 = 564
        ([0, 1], [0, 9], [0, 0, 1]),             # 10 + 90 = 100
        (
            [9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9],
            [8, 9, 9, 9, 0, 0, 0, 1],
        ),                                        # 9999999 + 9999 = 10009998
    ]


def main():
    cases = test_cases()

    for case_number, (digits1, digits2, expected) in enumerate(cases, start=1):
        l1 = to_linked_list(digits1)
        l2 = to_linked_list(digits2)

        result = to_list(add_two_numbers(l1, l2))

        assert result == expected, (
            f"Case {case_number} failed: "
            f"digits1={digits1}, "
            f"digits2={digits2}, "
            f"expected={expected}, "
            f"got={result}"
        )

        print(
            f"Case {case_number}: "
            f"{digits1} + {digits2} -> "
            f"{result} PASSED"
        )

    print(f"\nAll {len(cases)} tests passed!")


if __name__ == "__main__":
    main()