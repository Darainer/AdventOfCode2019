import unittest
from Day7_Amplification_Circuit.AmplificationConfig import CalculateMaxAmplification

phase_codes = [0, 1, 2, 3, 4]

class Test_program1(unittest.TestCase):
    def test_something(self):
        input_program = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        Max_Thruster_output = CalculateMaxAmplification(input_program, phase_codes)
        print('Max_Thruster_output',Max_Thruster_output)
        self.assertEqual(43210, Max_Thruster_output)

class Test_program2(unittest.TestCase):
    def test_something(self):
        input_program = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        Max_Thruster_output = CalculateMaxAmplification(input_program, phase_codes)
        print('Max_Thruster_output',Max_Thruster_output)
        self.assertEqual(54321, Max_Thruster_output)

class Test_program3(unittest.TestCase):
    def test_something(self):
        input_program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        Max_Thruster_output = CalculateMaxAmplification(input_program, phase_codes)
        print('Max_Thruster_output', Max_Thruster_output)
        self.assertEqual(65210, Max_Thruster_output)

class CompleteProgram(unittest.TestCase):
    def test_something(self):
        input_program = 'Day7_AMP_input_program.txt'
        Max_Thruster_output = CalculateMaxAmplification(input_program, phase_codes)
        print('Max_Thruster_output',  Max_Thruster_output)
        self.assertEqual(65210, Max_Thruster_output)

if __name__ == '__main__':
    unittest.main()
