
from pathlib import Path


def p1(steps):
    cur_pos = 50
    times_on_zero = 0

    for rot, dist in steps:
        if rot == "L":
            cur_pos -= dist
        elif rot == "R":
            cur_pos += dist

        cur_pos %= 100
        
        if cur_pos == 0:
            times_on_zero += 1

    return times_on_zero


def p2(steps):
    cur_pos = 50
    times_past_zero = 0

    for rot, dist in steps:
        while dist > 0:
            if rot == "L":
                cur_pos -= 1
                dist -= 1
            elif rot == "R":
                cur_pos += 1
                dist -= 1

            cur_pos %= 100
            
            if cur_pos == 0:
                times_past_zero += 1

    return times_past_zero


if __name__ == "__main__":
    filepath = Path("day1.txt")
    lines = filepath.read_text(encoding="utf-8").splitlines()
    steps = [(s[0], int(s[1:])) for s in lines]
    print(p1(steps))
    print(p2(steps))

