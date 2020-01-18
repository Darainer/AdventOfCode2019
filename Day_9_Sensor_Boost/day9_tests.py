import unittest
from IntCode import IntCode

class Day9_testcase1(unittest.TestCase):
    def test_something(self):
        input_program = [109, -1, 4, 1, 99]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([])
        self.assertEqual(-1, program_output[0])

class Day9_testcase2(unittest.TestCase):
    def test_something(self):
        input_program = [109, -1, 104, 1, 99]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([])
        self.assertEqual(1, program_output[0])

class Day9_testcase3(unittest.TestCase):
    def test_something(self):
        input_program = [109, -1, 204, 1, 99]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([])
        self.assertEqual(109, program_output[0])

class Day9_testcase4(unittest.TestCase):
    def test_something(self):
        input_program = [109, 1, 9, 2, 204, -6, 99]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([])
        self.assertEqual(204, program_output[0])

class Day9_testcase5(unittest.TestCase):
    def test_something(self):
        input_program = [109, 1, 109, 9, 204, -6, 99]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([])
        self.assertEqual(204, program_output[0])

class Day9_testcase6(unittest.TestCase):
    def test_something(self):
        input_program = [109, 1, 209, -1, 204, -106, 99]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([])
        self.assertEqual(204, program_output[0])

class Day9_testcase7(unittest.TestCase):
    def test_something(self):
        input_program = [109, 1, 3, 3, 204, 2, 99]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([1])
        self.assertEqual(input_program, program_output)

class Day9_testcase8(unittest.TestCase):
    def test_something(self):
        input_program = [109, 1, 203, 2, 204, 2, 99]
        myIntCoder = IntCode(input_program)
        program_output = myIntCoder.run_Intcode_with_input_output([1])
        self.assertEqual(input_program, program_output)

if __name__ == '__main__':
    unittest.main()
