coord_closest = [0, 0]


def manhattan_distance(coord):
    return abs(coord[0]) + abs(coord[1])


def closer_distance(current_distance, coord):
    new_distance = manhattan_distance(coord)
    if current_distance == 0:
        current_distance = new_distance
    smallest = current_distance if new_distance >= current_distance else new_distance
    return smallest


def minimize_delay(current_distance, coord, line1, line2):
    new_distance = line1.index(coord) + line2.index(coord) + 2
    if current_distance == 0:
        current_distance = new_distance
    smallest = current_distance if new_distance >= current_distance else new_distance
    return smallest


def solve2(lines):
    line1_positions = []
    line2_positions = []
    current_x = 0
    current_y = 0
    current_distance = 0

    lines = lines.splitlines()
    line1 = lines[0]
    compressed_line = line1.replace(' ', '')
    for direction in compressed_line.split(','):
        print(direction)
        direction_letter = direction[0]
        count = direction[1:]
        if direction_letter == 'R':
            for x in range(0, int(count)):
                current_x += 1
                line1_positions.append([current_x, current_y])
        if direction_letter == 'L':
            for x in range(0, int(count)):
                current_x -= 1
                line1_positions.append([current_x, current_y])
        if direction_letter == 'D':
            for x in range(0, int(count)):
                current_y += 1
                line1_positions.append([current_x, current_y])
        if direction_letter == 'U':
            for x in range(0, int(count)):
                current_y -= 1
                line1_positions.append([current_x, current_y])

    current_x = 0
    current_y = 0

    # now find the intersections with current position along line 2
    line2 = lines[1]
    compressed_line = line2.replace(' ', '')
    for direction in compressed_line.split(','):
        print(direction)
        direction_letter = direction[0]
        count = direction[1:]
        if direction_letter == 'R':
            for x in range(0, int(count)):
                current_x += 1
                line2_positions.append([current_x, current_y])
                if [current_x, current_y] in line1_positions:
                    current_distance = minimize_delay(current_distance, [current_x, current_y], line1_positions,
                                                      line2_positions)
        if direction_letter == 'L':
            for x in range(0, int(count)):
                current_x -= 1
                line2_positions.append([current_x, current_y])
                if [current_x, current_y] in line1_positions:
                    current_distance = minimize_delay(current_distance, [current_x, current_y], line1_positions,
                                                      line2_positions)
        if direction_letter == 'D':
            for x in range(0, int(count)):
                current_y += 1
                line2_positions.append([current_x, current_y])
                if [current_x, current_y] in line1_positions:
                    current_distance = minimize_delay(current_distance, [current_x, current_y], line1_positions,
                                                      line2_positions)
        if direction_letter == 'U':
            for x in range(0, int(count)):
                current_y -= 1
                line2_positions.append([current_x, current_y])
                if [current_x, current_y] in line1_positions:
                    current_distance = minimize_delay(current_distance, [current_x, current_y], line1_positions,
                                                      line2_positions)

    return current_distance


def solve(lines):
    line1_positions = []
    current_x = 0
    current_y = 0
    current_distance = 0

    lines = lines.splitlines()
    line1 = lines[0]
    compressed_line = line1.replace(' ', '')
    for direction in compressed_line.split(','):
        direction_letter = direction[0]
        count = direction[1:]
        if direction_letter == 'R':
            for x in range(0, int(count)):
                current_x += 1
                line1_positions.append([current_x, current_y])
        if direction_letter == 'L':
            for x in range(0, int(count)):
                current_x -= 1
                line1_positions.append([current_x, current_y])
        if direction_letter == 'D':
            for x in range(0, int(count)):
                current_y += 1
                line1_positions.append([current_x, current_y])
        if direction_letter == 'U':
            for x in range(0, int(count)):
                current_y -= 1
                line1_positions.append([current_x, current_y])

    current_x = 0
    current_y = 0

    # now find the intersections with current position along line 2
    line2 = lines[1]
    compressed_line = line2.replace(' ', '')
    for direction in compressed_line.split(','):
        direction_letter = direction[0]
        count = direction[1:]
        if direction_letter == 'R':
            for x in range(0, int(count)):
                current_x += 1
                if [current_x, current_y] in line1_positions:
                    current_distance = closer_distance(current_distance, [current_x, current_y])
        if direction_letter == 'L':
            for x in range(0, int(count)):
                current_x -= 1
                if [current_x, current_y] in line1_positions:
                    current_distance = closer_distance(current_distance, [current_x, current_y])
        if direction_letter == 'D':
            for x in range(0, int(count)):
                current_y += 1
                if [current_x, current_y] in line1_positions:
                    current_distance = closer_distance(current_distance, [current_x, current_y])
        if direction_letter == 'U':
            for x in range(0, int(count)):
                current_y -= 1
                if [current_x, current_y] in line1_positions:
                    current_distance = closer_distance(current_distance, [current_x, current_y])

    return current_distance
