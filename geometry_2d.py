import math as MathLib


class Point_2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = abs(self.x) + abs(self.y)  # taxicab_dist_to_origin

    def __add__(self, other):
        new_point = Point_2D(self.x + other.x, self.y + other.y)
        return new_point

def steps_between_points(first: Point_2D, second: Point_2D) ->int:
    steps = abs(first.x - second.x) + abs(first.y - second.y)
    return steps

class Line:
    def __init__(self, origin: Point_2D, end: Point_2D):
        self.Origin = origin
        self.End = end
        self.Length = self.calculate_length()
        if self.Length == 0:
            self.Angle_to_origin = -500
        else:
            self.Angle_to_origin = self.calculate_angle_to_origin()

    def calculate_length(self) -> int:
        x_steps = abs(self.End.x - self.Origin.x)
        y_steps = abs(self.End.y - self.Origin.y)
        return x_steps + y_steps

    def calculate_angle_to_origin(self):
        dx = (self.End.x - self.Origin.x)
        dy = (self.End.y - self.Origin.y)
        if dx != 0:
            slope = dy / dx
            angle_to_origin = MathLib.atan(slope)
        else:
            angle_to_origin = -500
        return angle_to_origin


class Line90Deg:
    def __init__(self, origin: Point_2D, end: Point_2D, steps_in: int):
        self.Origin = origin
        self.End = end
        self.Angle = int
        self.min_x = int
        self.max_x = int
        self.min_y = int
        self.max_y = int
        self.check_line_orientation()
        self.steps_origin = steps_in

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

    def steps_to_point(self, point: Point_2D) -> int:
        x_steps = abs(point.x - self.Origin.x)
        y_steps = abs(point.y - self.Origin.y)
        return x_steps + y_steps