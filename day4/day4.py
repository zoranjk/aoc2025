from time import time

def p1(map) -> int:
    max_rolls = 3

    adj_spots = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    accessible_spots = 0
    
    for col in map:
        for row in map[col]:
            ch = map[col][row]
            if ch == '.':
                continue
            adj_rolls = 0
            accessible = True
            for dx, dy in adj_spots:
                adj_x = col + dx
                adj_y = row + dy

                if adj_x in map and adj_y in map[adj_x]:
                    adj_ch = map[adj_x][adj_y]
                    if adj_ch == '@':
                        adj_rolls += 1
                
                if adj_rolls > max_rolls:
                    accessible = False
                    break

            if accessible:
                accessible_spots += 1

    return accessible_spots


def p2(map) -> int:
    max_rolls = 3

    adj_spots = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    accessible_spots = 0

    removed_roll = True

    while removed_roll:
        removed_roll = False

        new_map = map.copy()

        for col in map:
            for row in map[col]:
                ch = map[col][row]
                if ch == '.':
                    continue
                
                adj_rolls = 0
                accessible = True
                for dx, dy in adj_spots:
                    adj_x = col + dx
                    adj_y = row + dy

                    if adj_x in map and adj_y in map[adj_x]:
                        adj_ch = map[adj_x][adj_y]
                        if adj_ch == '@':
                            adj_rolls += 1
                    
                    if adj_rolls > max_rolls:
                        accessible = False
                        break

                if accessible:
                    accessible_spots += 1
                    new_map[col][row] = '.'
                    removed_roll = True

        map = new_map

    return accessible_spots


if __name__ == "__main__":
    start = time()
    with open("day4.txt", "r") as f:
        lines = f.readlines()

    map = {}

    for i, line in enumerate(lines):
        line = line.strip()
        map[i] = {}

        for j, ch in enumerate(line):

            map[i][j] = ch
            
    print(p1(map))
    print(p2(map))

    end = time()
    print(f"Execution time: {end - start} seconds")