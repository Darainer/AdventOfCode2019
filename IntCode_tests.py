import unittest
from IntCode import IntCode
from Day7_Amplification_Circuit.AmplificationConfig import CalculateMaxAmplification

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

class Day7_part1(unittest.TestCase):
    def test_something(self):
        phase_codes = [0, 1, 2, 3, 4]
        input_program = 'Day7_Amplification_Circuit/Day7_AMP_input_program.txt'
        Max_Thruster_output = CalculateMaxAmplification(input_program, phase_codes)
        print('Max_Thruster_output',  Max_Thruster_output)
        self.assertEqual(225056, Max_Thruster_output)

class Day9_part1testcase(unittest.TestCase):
    def test_something(self):
        input_program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([])
        self.assertEqual(input_program, program_output)

# class Day9_part1(unittest.TestCase):
#     def test_something(self):
#         input_program = 'Day_9_Sensor_Boost/Day9_input.txt'
#         myIntCoder = IntCode(input_program)
#         program_output = myIntCoder.run_Intcode_with_input_output([])
#         print('Boost Keycode',  program_output)
#         self.assertEqual(225056, program_output)

if __name__ == '__main__':
    unittest.main()
