from time import time


def has_equal_halves(num: int) -> bool:
    str_num = str(num)
    # odd length can't have equal halves
    if len(str_num) % 2 != 0:
        return False

    half_1 = str_num[:len(str_num)//2]
    half_2 = str_num[len(str_num)//2:]

    return half_1 == half_2


def p1(ranges) -> int:
    invalid_id_sum = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            if has_equal_halves(num):
                invalid_id_sum += num
            
    return invalid_id_sum


def has_repeated_sequence(num: int) -> bool:
    str_num = str(num)
    length = len(str_num)

    for divisor in range(2, length+1):
        if length % divisor != 0:
            continue

        seg_len = length // divisor
        segments = [str_num[i:i+seg_len] for i in range(0, length, seg_len)]

        if len(set(segments)) == 1:
            return True
    
    return False
        



def p2(ranges) -> int:
    invalid_id_sum = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            if has_repeated_sequence(num):
                invalid_id_sum += num
            
    return invalid_id_sum
            



if __name__ == "__main__":
    start = time()

    with open("day2.txt", "r") as f:
        lines = f.read().strip().split(",")

    ranges = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in lines]

    print(p1(ranges))
    print(p2(ranges))

    end = time()
    print(f"Execution time: {end - start} seconds")