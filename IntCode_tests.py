import unittest
from IntCode import IntCode
from Day2_IntCode.Day2_1202_Program_Alarm import find_inputs_for_computeResult
from Day7_Amplification_Circuit.AmplificationConfig import CalculateMaxAmplification, FeedbackAmplification

class Day2_part1(unittest.TestCase):
    def test_something(self):
        input_program = 'Day2_IntCode/Real_program_codes.txt'
        myIntcoder = IntCode(input_program)
        myIntcoder.program_codes[1] = 12
        myIntcoder.program_codes[2] = 2
        myIntcoder.compute_program()
        ret = myIntcoder.program_codes[0]
        self.assertEqual(4138658, ret )


class Day2_part2(unittest.TestCase):
    def test_something(self):
        input_program = 'Day2_IntCode/Real_program_codes.txt'
        myIntcoder = IntCode(input_program)
        ret = find_inputs_for_computeResult(myIntcoder,0, 99, 19690720)
        self.assertEqual(ret, 7264)

class Day5_part1(unittest.TestCase):
    def test_something(self):
        Input_day5 = 'Day5_Sunny_with_Asteroids/Day_5_input.txt'
        Intcoder = IntCode(Input_day5)
        Intcoder.run_Intcode_with_input(1)
        ret = Intcoder.output
        self.assertEqual(7988899,ret[-1])

class Day5_part2(unittest.TestCase):
    def test_something(self):
        Input_day5 = 'Day5_Sunny_with_Asteroids/Day_5_input.txt'
        Intcoder = IntCode(Input_day5)
        Intcoder.run_Intcode_with_input(5)
        ret = Intcoder.output
        self.assertEqual(13758663, ret[-1])

class Day7_part1(unittest.TestCase):
    def test_something(self):
        phase_codes = [0, 1, 2, 3, 4]
        input_program = 'Day7_Amplification_Circuit/Day7_AMP_input_program.txt'
        Max_Thruster_output = CalculateMaxAmplification(input_program, phase_codes)
        print('Max_Thruster_output',  Max_Thruster_output)
        self.assertEqual(225056, Max_Thruster_output)

class Day7Partb_Complete_program(unittest.TestCase):
    def test_something(self):
        phase_codes = [5, 6, 7, 8, 9]
        input_program = 'Day7_Amplification_Circuit/Day7_AMP_input_program.txt'
        Max_Thruster_output = FeedbackAmplification(input_program, phase_codes)
        print('Max_Thruster_output', Max_Thruster_output)
        self.assertEqual(14260332, Max_Thruster_output)

class Day9_part1testcase(unittest.TestCase):
    def test_something(self):
        input_program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([])
        self.assertEqual(input_program, program_output)


class Day9_part1testcase2(unittest.TestCase):
    def test_something(self):
        input_program = [1102,34915192,34915192,7,4,7,99,0]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([])
        self.assertEqual(len(str(abs(program_output[0]))),16)

class Day9_part1testcase3(unittest.TestCase):
    def test_something(self):
        input_program = [104,1125899906842624,99]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([])
        self.assertEqual(1125899906842624,program_output[0])

class Day9_part1(unittest.TestCase):
    def test_something(self):
        input_program = 'Day_9_Sensor_Boost/Day9_input.txt'
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output(1)
        print('Boost Keycode',  program_output)
        self.assertEqual(int, type(program_output[0]))

if __name__ == '__main__':
    unittest.main()
