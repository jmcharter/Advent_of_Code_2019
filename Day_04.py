'''
--- Day 4: Secure Container ---

You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet these criteria?

'''

puzzle_input = range(165432,707913)

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
        if password[step] == password[step -1]:
            has_duplicate = True
        step -= 1
    return True if has_duplicate else False


criteria_fit = [i for i in puzzle_input if check_criteria(i)]

print(len(criteria_fit))