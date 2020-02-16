import unittest

import Day10_Monitoring_Station.Day10_MonitoringStation as MonitoringStation

class Day10_testcase1(unittest.TestCase):
    def test_something(self):
        input_file = "test1.txt"
        output = MonitoringStation.find_best_monitoring_station(input_file)
        self.assertEqual(output[0], 33)
        self.assertEqual(output[1], 5)
        self.assertEqual(output[1], 8)

class Day10_Part1(unittest.TestCase):
    def test_something(self):
        input_file = "Day10_inputMap.txt"
        output = MonitoringStation.find_best_monitoring_station(input_file)
        print(output)
        #self.assertEqual(output[0], 33)
        #self.assertEqual(output[1], 5)
        #self.assertEqual(output[1], 8)

if __name__ == '__main__':
    unittest.main()
