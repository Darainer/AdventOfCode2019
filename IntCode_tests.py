import unittest
from IntCode import IntCode

class Day2_part1(unittest.TestCase):
    def test_something(self):
        input_program = 'Day2_IntCode/Real_program_codes.txt'
        myIntcoder = IntCode(input_program)
        myIntcoder.program_codes[1] = 12
        myIntcoder.program_codes[2] = 2
        myIntcoder.compute_program()
        ret = myIntcoder.program_codes[0]
        self.assertEqual(ret, 4138658)


class Day2_part2(unittest.TestCase):
    def test_something(self):
        input_program = 'Day2_IntCode/Real_program_codes.txt'
        myIntcoder = IntCode(input_program)
        ret = myIntcoder.find_inputs_for_computeResult(0, 99, 19690720)
        self.assertEqual(ret, 7264)

class Day5_part1(unittest.TestCase):
    def test_something(self):
        Input_day5 = 'Day5_Sunny_with_Asteroids/Day_5_input.txt'
        Intcoder = IntCode(Input_day5)
        Intcoder.run_Intcode_with_input(1)
        ret = Intcoder.output
        self.assertEqual(ret, 7988899)

class Day5_part2(unittest.TestCase):
    def test_something(self):
        Input_day5 = 'Day5_Sunny_with_Asteroids/Day_5_input.txt'
        Intcoder = IntCode(Input_day5)
        Intcoder.run_Intcode_with_input(5)
        ret = Intcoder.output
        self.assertEqual(ret, 13758663)


if __name__ == '__main__':
    unittest.main()
