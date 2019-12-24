
def split_int_to_list(int_number: int) -> list:
    digit_list = []
    while int_number > 0:
        digit_list.append(int_number % 10)
        int_number //= 10
    digit_list.reverse()
    return digit_list

def test_for_repeating_digits(digits: list)->bool:
    i = 1
    while i != len(digits):
        if digits[i] == digits[i-1]:
            return True
        else:
            i = i + 1
    return False

def get_diff(digits: list) -> list:
    Diff = []
    for i in range(1, len(digits)):
        Diff.append(digits[i]-digits[i-1])
    return Diff

def test_for_double_digits_only(digits: list)->bool:
# numbers are ascending
    diff = get_diff(digits)
    count = 0
    for i in range(len(diff)):
        if diff[i] == 0:
            count += 1
        else:
            if count == 1:
                return True
            else:
                count = 0
        if count == 1 and i == (len(diff)-1):
            return True
    return False


def test_for_ascending_digits(digits: list)->bool:
    i = 1
    while i != len(digits):
        if digits[i] >= digits[i-1]:
            i = i + 1
        else:
            return False
    return True

####

start_value = 138241
end_value = 674034
range_int =range( start_value, end_value)


### tests

int_list = []
test_value = 234456
int_list = split_int_to_list(test_value)
has_repeating_digits = test_for_double_digits_only(int_list)


###
potential_PWs = []

for int in range_int:
    int_list = split_int_to_list(int)
    has_ascending_digits = test_for_ascending_digits(int_list)
    if has_ascending_digits: # can assume ascending in test
        has_repeating_digits = test_for_double_digits_only(int_list)
    else:
        has_repeating_digits= False
    if has_ascending_digits and has_repeating_digits:
        potential_PWs.append(int)

print("in range", start_value, "to", end_value)
print("the number_of_potential_PWs =", len(potential_PWs))


