# parse input to an Asteroid map Data Structure
input_file = 'Day10_inputMap.txt'


def parse_input_map(input_file) -> list:
    AsteriodMap = []
    with open(input_file, 'r') as file:
        input_text_lines = file.readlines()
        for line in input_text_lines:
            row = []
            for char in line:
                if char == "#":
                    row.append(1)
                elif char == ".":
                    row.append(0)
            AsteriodMap.append(row)
    return AsteriodMap


AsteriodMap = parse_input_map(input_file)
for row in AsteriodMap:
    print(row)
# we have column 0 and row 0
print("element (2,2) = ", AsteriodMap[1][1])

