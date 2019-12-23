import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import colors as mcolors



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
        self.Angle = int
        self.min_x = int
        self.max_x = int
        self.min_y = int
        self.max_y = int
        self.check_line_orientation()

    def check_line_orientation(self):
        if self.End.x == self.Origin.x:
            self.min_x = self.max_x = self.End.x
            if self.End.y > self.Origin.y:
                self.Angle = 90
                self.max_y = self.End.y
                self.min_y = self.Origin.y
            else:
                self.max_y = self.Origin.y
                self.min_y = self.End.y
                self.Angle = -90
        elif self.End.y == self.Origin.y:
            self.min_y = self.max_y = self.End.y
            if self.End.x > self.Origin.x:
                self.Angle = 0
                self.max_x = self.End.x
                self.min_x = self.Origin.x
            else:
                self.Angle = 180
                self.max_x = self.Origin.x
                self.min_x = self.End.x


class GridPoint:
    def __init__(self):
        self.Wire1Contact = False
        self.Wire2Contact = False

    def __repr__(self):
        return "Wire1Contact is %s, Wire1Contact is %s" % (self.Wire1Contact, self.Wire2Contact)

    def __str__(self):
        return "Wire1Contact is %s, Wire1Contact is %s" % (self.Wire1Contact, self.Wire2Contact)

def FindMinCommonValue(v1, v2, q1, q2) -> int:

    if v1 <= q1 <= v2 or v1 <= q2 <= v2:
        # overlap exists
        closest_1 = min(abs(v1), abs(v2))
        closest_2 = min(abs(q1), abs(q2))
        if closest_1 < closest_2:
            return closest_2
        else:
            return closest_1
    else:
        return -1

def linesareParallel(line1: Line, line2: Line) -> bool:
    lines_are_parallel = False
    if (line1.Angle == 90 or line1.Angle == -90) and (line2.Angle == 90 or line2 == -90):
        lines_are_parallel = True
    if (line1.Angle == 0 or line1.Angle == 180) and (line2.Angle == 0 or line2 == 180):
        lines_are_parallel = True
    else:
        lines_are_parallel = False
    return lines_are_parallel


def CheckIntersection(line1: Line, line2: Line) -> point_2D:
    point = point_2D(0, 0)
    if linesareParallel(line1, line2):
        if (line1.Angle == 90 or -90) and line1.Origin.x == line2.Origin.x:
            # lines are collinear x plane
            y_common_min = FindMinCommonValue(line1.Origin.y, line1.End.y, line2.Origin.y, line2.End.y)
            if y_common_min != -1:
                return point_2D(line1.Origin.x, y_common_min)
        if (line1.Angle == 0 or 180) and line1.Origin.y == line2.Origin.y:
            # lines are collinear y plane
            x_common_min = FindMinCommonValue(line1.Origin.x, line1.End.x, line2.Origin.x, line2.End.x)
            if x_common_min != -1:
                return point_2D(x_common_min, line1.Origin.y)
    else:
        # lines are perpendicular
        if (line1.Angle == 0 or 180) and (line1.min_x <= line2.Origin.x <= line1.max_x):
            # x overlap
            if line2.min_y <= line1.Origin.y <= line2.max_y:
            # x and y overlap: vertical line 2 is crossing horizontal line 1 at line2.x
                return point_2D(line2.Origin.x, line1.Origin.y)

        if (line2.Angle == 0 or 180) and (line2.min_x <= line1.Origin.x <= line2.max_x):
            #x overlap
            if line1.min_y <= line2.Origin.y <= line1.max_y:
            #x and y overlap  vertical line 1 is crossing horizontal line 2 at line1.x
                return point_2D(line1.Origin.x, line2.Origin.y)

    return point


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

def plot_segments(segment):
    x = [0]
    y = [0]
    for seg in segment.Segment:
        x.append(seg.End.x)
        y.append(seg.End.y)
    plt.plot(x, y)

# process
input_file = "Day3_Crossed_wires.txt"
#input_file = "crossedwiretest.txt"
#input_file = "crossedwiretest2.txt"
#input_file = "simpletest.txt"
plot_active = True

# parse commands from txt file
with open(input_file, 'r') as file:
    program_input1 = file.readline()
    program_input1 = program_input1.strip('\n')
    Commands_wire1 = program_input1.split(',')
    program_input2 = file.readline()
    Commands_wire2 = program_input2.split(',')

Wire1_segments = ProcessCommandsToWireSegments(Commands_wire1)
Wire2_segments = ProcessCommandsToWireSegments(Commands_wire2)

if plot_active:
    plot_segments(Wire1_segments)
    plot_segments(Wire2_segments)
    plt.show()

# check intersections
list_of_intersection_points = []
ck = point_2D
for segment1 in Wire1_segments.Segment:
    for segment2 in Wire2_segments.Segment:
        ck = CheckIntersection(segment1, segment2)
        if ck.dist != 0:
            list_of_intersection_points.append(ck)

list_of_intersection_points.sort(key=lambda point: point.dist)
print(list_of_intersection_points[0].dist)


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
