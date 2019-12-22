from IntCode import IntCode
import pickle
#### instances

simpleInput = [1,9,10,3,2,3,11,0,99,30,40,50]
simpleOutputFile = "output_simple_programcodes.txt"
Intcoder = IntCode(simpleInput, simpleOutputFile)
Intcoder.write_output()

##

simpleInput2 = [1,1,1,4,99,5,6,0,99]
simpleOutputFile2 = "output_simple_programcodes2.txt"
#test2 = tuple(simpleInput2, simpleOutputFile2)
Intcoder = IntCode(simpleInput2, simpleOutputFile2)
Intcoder.write_output()

test_in3 = [2,4,4,5,99,0]
Inttest3 = IntCode(test_in3,"test3_out")


testOut3 = [2,4,4,5,99,9801]

#parse input file into operational lines
RealinputFile = "Real_program_codes.txt"
RealoutputFile = "1202_Program_output.txt"


Intcoder_real = IntCode(RealinputFile, RealoutputFile)
Intcoder_real.write_output()

IntCoder_part2 = IntCode(RealinputFile, "ReverseEng.txt")
IntCoder_part2.find_inputs_for_computeResult(0, 99, 19690720)

