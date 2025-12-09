from typing import Tuple, List
from time import time

def p1(battery_banks: List[str]) -> int:
    max_joltages = []
    for bb in battery_banks:
        lm_max_digit, index = leftmost_max_digit(bb)
        f_max_digit, f_index = first_max_digit(bb, index + 1)
        max_joltages.append(str(lm_max_digit) + str(f_max_digit))

    return sum(int(joltage) for joltage in max_joltages)

def first_max_digit(s: str, start_index: int) -> Tuple[int, int]:
    max_digit = -1
    index = -1
    for i in range(start_index, len(s)):
        digit = int(s[i])
        if digit > max_digit:
            max_digit = digit
            index = i
            if max_digit == 9:
                return max_digit, index
    return max_digit, index

def leftmost_max_digit(s: str) -> Tuple[int, int]:
    max_digit = -1
    index = -1
    for i, ch in enumerate(s):
        digit = int(ch)
        if digit > max_digit and i < len(s) - 1:
            max_digit = digit
            index = i
            if max_digit == 9:
                return max_digit, index
    return max_digit, index


def lm_max_digit_with_space_to_right(s: str, digits_needed: int) -> Tuple[int, int]:
    max_digit = -1
    index = -1
    for i in range(0, len(s) - digits_needed):
        str_digit = s[i]
        digit = int(str_digit)
        if digit > max_digit and i < len(s) - digits_needed:
            max_digit = digit
            index = i
            if max_digit == 9:
                break


    return max_digit, index


def p2(battery_banks: List[str]) -> int:
    joltage = 0
    for bb in battery_banks:
        digits_needed = 12
        digits = []
        start_index = 0
        while digits_needed > 0:
            lm_max_digit, start_index = lm_max_digit_with_space_to_right(bb, digits_needed-1)
            
            digits.append(str(lm_max_digit))

            bb = bb[start_index+1:]
            digits_needed -= 1
        
        max_joltage = int("".join(digits))
        joltage += max_joltage

    return joltage








if __name__ == "__main__":
    start = time()
    with open("day3.txt", "r") as f:
        lines = f.readlines()

    battery_banks = [line.strip() for line in lines]

    print(p1(battery_banks))
    print(p2(battery_banks))
    end = time()
    print(f"Execution time: {end - start} seconds")