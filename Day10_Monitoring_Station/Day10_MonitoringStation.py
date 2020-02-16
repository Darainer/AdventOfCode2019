from geometry_2d import Point_2D, Line


class Asteroid:
    def __init__(self, location: Point_2D):
        self.location = location
        self.detections_as_base = -1
        self.line_to_current_base = Line(Point_2D(0,0), self.location)

    def set_parameters_to_base(self, base_location: Point_2D):
        self.line_to_current_base = Line(base_location, self.location)

    def set_detections(self, detections: int):
        self.detections_as_base = detections

    def __repr__(self):
        return repr((self.location.x, self.location.y, self.line_to_current_base.Length, self.line_to_current_base.Angle_to_origin))


def parse_input_file(input_file) -> [list, list]:
    AsteroidMap = []
    AsteroidList = []
    with open(input_file, 'r') as file:
        input_text_lines = file.readlines()

        for row_index, line in enumerate(input_text_lines):
            row = []
            for col_index, char in enumerate(line):
                if char == "#":
                    row.append(1)
                    AsteroidList.append(Asteroid(Point_2D(row_index, col_index)))
                elif char == ".":
                    row.append(0)
            AsteroidMap.append(row)
    return AsteroidMap, AsteroidList


def print_asteroid_map(AsteroidMap):
    for row in AsteroidMap:
        print(row)


def find_best_monitoring_station(input_filename) -> list:  # [Detections, x pos,y pos]
    [AsteroidMap, AsteroidList] = parse_input_file(input_filename)

    for asteroid_base in AsteroidList:
        # try each one as a base
        for neighbor_asteroid in AsteroidList:
            neighbor_asteroid.set_parameters_to_base(asteroid_base.location)
        AsteroidList.sort(key=lambda ast: ast.line_to_current_base.Length)
        AsteroidList.sort(key=lambda ast: ast.line_to_current_base.Angle_to_origin)
        for i, myAsteroid in enumerate(AsteroidList):

            if myAsteroid.location != asteroid_base.location:
                if myAsteroid == AsteroidList[-1]:
                    if myAsteroid.line_to_current_base.Angle_to_origin != AsteroidList[i-1].line_to_current_base.Angle_to_origin:
                        asteroid_base.detections_as_base += 1
                elif myAsteroid.line_to_current_base.Angle_to_origin != AsteroidList[i+1].line_to_current_base.Angle_to_origin:
                    asteroid_base.detections_as_base += 1

    AsteroidList.sort(key=lambda ast: ast.detections_as_base, reverse=True)
    return [AsteroidList[0].detections_as_base, AsteroidList[0].location.x, AsteroidList[0].location.y]
