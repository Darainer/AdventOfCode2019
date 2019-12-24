
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
test_value = 123267
int_list = split_int_to_list(test_value)
#has_repeating_digits = test_for_repeating_digits(int_list)
#has_ascending_digits = test_for_ascending_digits(int_list)

###
potential_PWs = []

for int in range_int:
    int_list = split_int_to_list(int)
    has_repeating_digits = test_for_repeating_digits(int_list)
    has_ascending_digits = test_for_ascending_digits(int_list)
    if has_ascending_digits and has_repeating_digits:
        potential_PWs.append(int)

print("in range", start_value, "to", end_value)
print("the number_of_potential_PWs =", len(potential_PWs))



#run through the range
#convert to list of int

#test_1: contains two adjacent digits
#for ind in start_value:
    #if ind == start_value[:1]:

#test 2: two adjacent digits are the same
    #run through for each

#test 3: ascending numbers

