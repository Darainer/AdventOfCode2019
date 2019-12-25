from IntCode import IntCode

# simpleInput_opcode3 = [3,0,4,0,99]
# simpleOutputFile = "output_simple_programcodes.txt"
# Intcoder = IntCode(simpleInput_opcode3, simpleOutputFile)
# output = Intcoder.run_Intcode_with_input_output(43)
# print(output)

# simpleInput_opcode2 = [1002,4,3,4,33]
# simpleOutputFile = "output_simple_programcodes.txt"
# Intcoder = IntCode(simpleInput_opcode2, simpleOutputFile)
# output = Intcoder.run_Intcode_with_input_output(43)
# print(output)

simpleInput_opcode2 = "Day_5_input.txt"
simpleOutputFile = "output_programcodes.txt"
Intcoder = IntCode(simpleInput_opcode2, simpleOutputFile)
Intcoder.run_Intcode_with_input(1)

Intcoder.write_output()
