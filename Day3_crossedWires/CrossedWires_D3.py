import numpy as np

class point_2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = abs(self.x) + abs(self.y)  # taxicab_dist_to_origin

    def __add__(self, other):
        new_point = point_2D(self.x + other.x, self.y + other.y)
        return new_point

class Line:
    def __init__(self, origin: point_2D, end: point_2D):
        self.Origin = origin
        self.End = end
        self.OrientationAngle = int
        self.check_line_orientation()

    def check_line_orientation(self):
        if self.End.x == self.Origin.x:
            self.OrientationAngle = 0
        elif self.End.y == self.Origin.y:
            self.OrientationAngle = 90
        else:
            self.OrientationAngle = -1

class GridPoint:
    def __init__(self):
        self.Wire1Contact = False
        self.Wire2Contact = False

    def __repr__(self):
        return "Wire1Contact is %s, Wire1Contact is %s" % (self.Wire1Contact, self.Wire2Contact)

    def __str__(self):
        return "Wire1Contact is %s, Wire1Contact is %s" % (self.Wire1Contact, self.Wire2Contact)

def FindMinCommonValue(p1,p2,q1,q2) -> int:


def CheckIntersection(line1: Line, line2: Line): # -> point_2D:
        if line1.OrientationAngle == line2.OrientationAngle:
            # lines_are_parallel
            if line1.OrientationAngle == 90 & line1.Origin.x == line2.Origin.x:
                # lines are collinear x plane
                y_common_min = find_min_common(line1.Origin.x, line1.End.x, line2.Origin.x, line2.End.x)
                if y_common_min != -1:
                    return point_2D(line1.Origin.x, y_common_min)
            if line1.OrientationAngle == 0:
                # lines are collinear y plane
                x_common_min = find_min_common(line1.Origin.x, line1.End.x, line2.Origin.x, line2.End.x)
                if x_common_min != -1:
                    return point_2D(x_common_min, line1.Origin.y)
        elif line1.OrientationAngle != line2.OrientationAngle:
            # lines are perpendicular
            if line1.OrientationAngle == 0 & (line2.Origin.x in range(line1.Origin.x, line1.End.x)):
                # vertical line 2 is crossing horizontal line 1 at line2.x
                return point_2D(line2.Origin.x, line1.Origin.y)
            if line1.OrientationAngle == 90 & (line2.Origin.y in range(line1.Origin.y, line1.End.y)):
                # Horizontal line 2 is crossing vertical line 1 at line2.x
                return point_2D(line1.Origin.x, line2.Origin.y)

class ProcessCommandsToWireSegments:
    def __init__(self, commands):

        self.commands = commands
        self.Segment = []
        self.get_segments()

    def get_segments(self):
        Currentpoint = point_2D(0, 0)
        for it in range(len(self.commands)):
            end_point = self.return_endpoint_after_command(self.commands[it], Currentpoint)
            self.Segment.append(Line(Currentpoint, end_point))
            Currentpoint = end_point

    def return_endpoint_after_command(self, command, origin: point_2D) -> point_2D:
        end_point = point_2D(0, 0)
        if command[0] == "U":
            end_point = origin + point_2D(0, int(command[1:]))
        elif command[0] == "D":
            end_point = origin + point_2D(0, -int(command[1:]))
        elif command[0] == "L":
            end_point = origin + point_2D(-int(command[1:]), 0)
        elif command[0] == "R":
            end_point = origin + point_2D(int(command[1:]), 0)
        else:
            print("wtf")
        return end_point


# process
input_file = "Day3_Crossed_wires.txt"

# parse commands from txt file
with open(input_file, 'r') as file:
    program_input1 = file.readline()
    Commands_wire1 = program_input1.split(',')
    program_input2 = file.readline()
    Commands_wire2 = program_input2.split(',')

Wire1_segments = ProcessCommandsToWireSegments(Commands_wire1)
Wire2_segments = ProcessCommandsToWireSegments(Commands_wire2)

# check intersections
list_of_intersection_points = []
for segment1 in Wire1_segments.Segment:
    for segment2 in Wire2_segments.Segment:
        point = CheckIntersection(segment1, segment2)
        ck = CheckIntersection(Wire1_segments.Segment[1], Wire2_segments.Segment[1])
        list_of_intersection_points.append(ck)

print(len(list_of_intersection_points))

#
# print(Direction1[1].keys(), Direction1[1].items())
#
#
#
# Grid = np.ndarray(shape=[1000, 1000], dtype=GridPoint)
# Grid.dtype
# print(Grid[10][1])
# for i in range(Grid[1][:]):
#     i = GridPoint

# Method 1

# allocate a grid to set a flag at a passed point ( static, dynamic for each move or size estimate)
# each array element a struct with (bool)WIRE1, (bool)WIRE2
# when tracing out the second wire, check if the flag is set for the first one
# create a (linked) list which points to elements where both values are set
# 
# trace out the two

# Method 2

# consider the wire paths as individual line segments
# we are not interested in where the segments cross each other, rather only where they cross each other
# parse both the wires  into a list of elements
# check each of the segments of the first wire for crossing with the second wire segments
# intersecting line algo
