def solution(s: str) -> int:
    roman_map = {
        "I": 1,
        "V": 5, 
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    n = 0
    
    for i, c in enumerate(s):
        # flag = False
        # if i < s.__len__() - 1:
        #     nextC = s[i+1]
        #     if c == 'I' and (nextC == 'V' or nextC == 'X'):
        #         n-=1
        #         flag = True
        #     if c == 'X' and (nextC == 'L' or nextC == 'C'):
        #         n-=10
        #         flag = True
        #     if c == 'C' and (nextC == 'D' or nextC == 'M'):
        #         n-=100
        #         flag = True
        # if flag == False:
        #     n += roman_map[c]

        current = roman_map[s[i]]

        if i + 1 < len(s) and current < roman_map[s[i + 1]]:
            n -= current
        else:
            n += current
            

    return n

def test_cases():
    return [
        ("I", 1),          # Smallest single numeral
        ("III", 3),        # Repeated numeral
        ("IV", 4),         # Subtraction case
        ("IX", 9),         # Subtraction case
        ("LVIII", 58),     # Mixed addition
        ("XL", 40),        # X before L
        ("XC", 90),        # X before C
        ("CD", 400),       # C before D
        ("CM", 900),       # C before M
        ("MCMXCIV", 1994), # Multiple subtraction cases
        ("MMMCMXCIX", 3999), # Largest standard Roman numeral
    ]


def main():
    tests = test_cases()

    for i, (roman, expected) in enumerate(tests, start=1):
        result = solution(roman)

        if result == expected:
            print(f"Test {i}: {roman} -> {result} PASSED")
        else:
            print(
                f"Test {i}: {roman} -> {result} "
                f"FAILED (expected {expected})"
            )


if __name__ == '__main__':
    main()