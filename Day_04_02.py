'''
--- Part Two ---

An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

    112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
    123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
    111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).

How many different passwords within the range given in your puzzle input meet all of the criteria?

'''

puzzle_input = range(165432,707912+1)

# Make sure all digits - going from left to right - always decrease.
def check_criteria(password):
    password = str(password)
    step = len(password) - 1
    has_duplicate = False
    while step > 0:
        # While loop first checks that sequential digits don't decrease,
        # then it compares digits for duplicates. As long as at least
        # one digit is duplicate, dup check will be set to True. If not
        # the function will return false.
        if password[step] >= password[step - 1]:
            pass
        else:
            return False
        # Check if the current digit is equal to the next, and also that the current
        # digit occurs no more than twice.
        if password[step] == password[step -1] and [i for i in password].count(password[step]) <= 2:
            has_duplicate = True
        step -= 1
    return True if has_duplicate else False


criteria_fit = [i for i in puzzle_input if check_criteria(i)]

print(len(criteria_fit))
