from time import time

def p1(ranges, numbers) -> int:
    count = 0

    for number in numbers:
        for start, end in ranges:
            if start <= number <= end:
                count += 1
                break

    return count


def p2(ranges) -> int:
    sorted_ranges = sorted(ranges)
    
    merged_ranges = [sorted_ranges[0]]
    
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged_ranges[-1]
        
        # If current range overlaps with last range, merge them
        if current_start <= last_end + 1:
            merged_ranges[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add as new range
            merged_ranges.append((current_start, current_end))

    covered = 0

    for start, end in merged_ranges:
        covered += (end - start + 1)

    return covered
        
        
if __name__ == "__main__":
    start = time()
    with open("day5.txt", "r") as f:
        lines = f.read().strip().split("\n\n")  # Split sections by blank line

    # First section: Parse ranges into tuples
    ranges = [tuple(map(int, line.split('-'))) for line in lines[0].splitlines()]

    # Second section: Parse single integers
    numbers = [int(line) for line in lines[1].splitlines()]

    print(p1(ranges, numbers))

    print(p2(ranges))

    end = time()
    print(f"Execution time: {end - start} seconds")