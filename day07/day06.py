import time

def create_hell_map(path):
    with open(path) as file:
        input = file.read().strip().split('\n')
        return [list(line) for line in input]

def print_map(map):
    for line in map:
        print("".join(line))

def get_guard_position(map):
    for line_number, line in enumerate(map):
        if "^" in line:
            return line.index("^"), line_number
    return None, None

def set_map(map, x, y, symbol):
    map[x][y] = symbol

def count_distinct_pos(map):
    print_map(map)
    guard = get_guard_position(map)
    guard_direction = (0, -1)
    guard_char = ['^', '>', 'v', '<']
    rotation = 0
    while (0 <= guard[0] < len(map[0])) and (0 <= guard[1] < len(map)):
        next_position = (guard[0] + guard_direction[0], guard[1] + guard_direction[1])
        if (0 <= next_position[0] < len(map[0])) and (0 <= next_position[1] < len(map)):
            print("Next Position is in map")
            if map[next_position[1]][next_position[0]] == '#' :
                print("Next is Obstacle")
                rotation = (rotation + 1) % 4
                guard_direction = (-guard_direction[1], guard_direction[0])
                next_position = (guard[0] + guard_direction[0], guard[1] + guard_direction[1])
            if map[next_position[1]][next_position[0]] == '.' or map[next_position[1]][next_position[0]] == 'X' :
                print("Next is either '. or 'X'")
            set_map(map, guard[1], guard[0], "X")
            set_map(map, next_position[1], next_position[0], guard_char[rotation])
            guard = next_position
        else:
            print("Next_position is out")
            set_map(map, guard[1], guard[0], "X")
            break
    print_map(map)
    return sum([line.count("X") for line in map])

def get_possible_obs_positions(map):
    possible_pos = [
    (row, col)
    for row in range(len(map))
    for col in range(len(map[0]))
    if map[row][col] == "."
    ]
    return possible_pos

def simulate_guard(map):
    guard = get_guard_position(map)
    guard_direction = (0, -1)  # Start direction (up)
    guard_char = ['^', '>', 'v', '<']
    rotation = 0
    states = set()
    while True:
        state = (guard, guard_direction)
        if state in states:
            return True
        states.add(state)
        next_position = (guard[0] + guard_direction[0], guard[1] + guard_direction[1])

        if not (0 <= next_position[1] < len(map) and 0 <= next_position[0] < len(map[0])):
            return False

        if map[next_position[1]][next_position[0]] in ['#', 'O']:
            # Rotate clockwise on obstacle
            rotation = (rotation + 1) % 4
            guard_direction = (-guard_direction[1], guard_direction[0])

        elif map[next_position[1]][next_position[0]] == '.' or map[next_position[1]][next_position[0]] == 'X':
            # Move forward
            set_map(map, guard[1], guard[0], 'X')  # Mark current position
            set_map(map, next_position[1], next_position[0], guard_char[rotation])  # Move guard
            guard = next_position
        else:
            break  # Stuck in a loop or invalid
    return False

def find_stuck_loop_positions(map):
    possible_positions = get_possible_obs_positions(map)
    count = 0
    for pos in possible_positions:
        test_map = [list(row) for row in map]  # Deep copy of the map
        test_map[pos[0]][pos[1]] = 'O'  # Add obstruction
        if simulate_guard(test_map):  # Check if obstruction causes a loop
            count += 1
    return count

if __name__ == "__main__":
    print("---Part One---")
    map_test = create_hell_map('input-example-day06-part1.txt')
    print("Test input: ", count_distinct_pos(map_test))
    map_input = create_hell_map('input-day06.txt')
    print("Total number of distinct positions: ", count_distinct_pos(map_input))
    print("---Part Two---")
    map_test = create_hell_map('input-example-day06-part1.txt')
    print("Test input: ", find_stuck_loop_positions(map_test))
    map_input = create_hell_map('input-day06.txt')
    start_time = time.time()  # Start timing
    print("Number of valid positions for obstructions: ", find_stuck_loop_positions(map_input))
    end_time = time.time()  # End timing
    print(f"Execution time: {end_time - start_time:.2f} seconds")