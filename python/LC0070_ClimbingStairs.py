def recursive_solution(n: int) -> int:
    if n <= 2:
        return n

    return recursive_solution(n - 1) + recursive_solution(n - 2)


# Bottom-up dynamic programming
# Optimized for constant space
#
# Idea:
# ways(n) = ways(n - 1) + ways(n - 2)
#
# To reach stair n, your final move must come from:
# 1. stair n - 1, then take 1 step
# 2. stair n - 2, then take 2 steps
def dp_solution(n: int) -> int:
    if n <= 2:
        return n

    first = 1
    second = 2

    for _ in range(3, n + 1):
        # [1, 2] -> [2, 3] -> [3, 5] -> [5, 8]
        first, second = second, first + second

    return second


def test_cases():
    return [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (10, 89),
        (20, 10946),
    ]


def main():
    cases = test_cases()

    for solution in (recursive_solution, dp_solution):
        print(f"\nTesting {solution.__name__}")

        for i, (stairs, expected) in enumerate(cases, start=1):
            result = solution(stairs)

            assert result == expected, (
                f"Test {i} failed: "
                f"stairs={stairs}, "
                f"expected={expected}, "
                f"got={result}"
            )

            print(
                f"Test {i}: stairs={stairs}, "
                f"expected={expected}, "
                f"result={result} PASSED"
            )


if __name__ == "__main__":
    main()