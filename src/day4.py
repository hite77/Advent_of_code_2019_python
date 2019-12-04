def is_valid(number):
    return contains_at_least_one_duplicate(number)


def contains_at_least_one_duplicate(number):
    string_number = str(number)
    for x in range(0, len(string_number)-1):
        if string_number[x] == string_number[x+1]:
            return True
    return False

# range 178416-676461
