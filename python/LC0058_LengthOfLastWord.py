def solution(s: str) -> int:
    return len(s.split()[-1])


def test_cases():
    cases = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("a", 1),
        ("Python", 6),
        ("hello     world", 5),
    ]

    for s, expected in cases:
        result = solution(s)

        print(f"Input:    {s!r}")
        print(f"Expected: {expected}")
        print(f"Result:   {result}")

        assert result == expected, (
            f"FAILED -> Expected {expected}, but got {result}"
        )

        print("✅ PASSED")
        print("-" * 40)


def main():
    test_cases()
    print("🎉 All test cases passed!")


if __name__ == "__main__":
    main()