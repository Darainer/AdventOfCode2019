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

def print_asteroid_map(AsteroidMap):
    for row in AsteriodMap:
        print(row)


class point_2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = abs(self.x) + abs(self.y)  # taxicab_dist_to_origin

    def __add__(self, other):
        new_point = point_2D(self.x + other.x, self.y + other.y)
        return new_point



def steps_between_points(first: point_2D, second: point_2D) ->int:
    steps = abs(first.x - second.x) + abs(first.y - second.y)
    return steps

class Asteroid:
    def __init__(self, location: point_2D):
        self.location = location
        #self.blocked = False


AsteriodMap = parse_input_map(input_file)
print_asteroid_map(AsteriodMap)

# we have column 0 and row 0
print("element (2,2) = ", AsteriodMap[1][1])


# fill a list of all asteriods:
row_index = 0
col_index = 0
AsteroidList = []
for Row in AsteriodMap:
    for Asteroid_at_Location in Row:
        if Asteroid_at_Location == True:
            location = point_2D(row_index,col_index)
            AsteroidList.append(Asteroid(location))
        col_index +=1
    row_index +=1

CurrentAsteroid = AsteroidList[57]
AsteroidList.sort(key=lambda asteroid: steps_between_points(asteroid.location, CurrentAsteroid.location))
print("dist" ,AsteroidList[57].location.dist)