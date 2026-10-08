def solution(words: list[str]) -> str:
    if not words:
        return ""

    smallest_len = min(len(word) for word in words)

    for i in range(smallest_len):
        char = words[0][i]

        for word in words:
            if word[i] != char:
                return words[0][:i]

    return words[0][:smallest_len]


def test_cases():
    cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["throne", "throne"], "throne"),
        (["a"], "a"),
        (["ab", "a"], "a"),
        ([], ""),
    ]

    for words, expected in cases:
        result = solution(words)

        print(f"Input:    {words}")
        print(f"Expected: {expected!r}")
        print(f"Result:   {result!r}")

        assert result == expected, (
            f"FAILED -> Expected {expected!r}, but got {result!r}"
        )

        print("✅ PASSED")
        print("-" * 40)


def main():
    test_cases()
    print("🎉 All test cases passed!")


if __name__ == "__main__":
    main()