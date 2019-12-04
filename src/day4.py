def count_valid_for_range(start, end):
    count = 0
    for x in range(start, end):
        if is_valid(x):
            count += 1
    return count


def count_valid_for_range_part_two(start, end):
    count = 0
    for x in range(start, end):
        if contains_double_matches(x) and \
                numbers_increase_or_stay_same_from_left_to_right(x):
            count += 1
    return count


def is_valid(number):
    return contains_at_least_one_duplicate(number) and \
           numbers_increase_or_stay_same_from_left_to_right(number)


def contains_at_least_one_duplicate(number):
    string_number = str(number)
    for x in range(0, len(string_number)-1):
        if string_number[x] == string_number[x+1]:
            return True
    return False


def contains_double_matches(number):
    string_number = str(number)
    for x in range(0, len(string_number)-1):
        if string_number[x] == string_number[x + 1]:
            valid = True
            if x > 0 and string_number[x-1] == string_number[x]:
                valid = False
            if x + 2 < len(string_number) and string_number[x+2] == string_number[x]:
                valid = False
            if valid:
                return True
    return False


def numbers_increase_or_stay_same_from_left_to_right(number):
    string_number = str(number)
    for x in range(0, len(string_number)-1):
        if int(string_number[x]) > int(string_number[x+1]):
            return False
    return True
