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

# simpleInput_opcode2 = "Day_5_input.txt"
# simpleOutputFile = "output_programcodes.txt"
# Intcoder = IntCode(simpleInput_opcode2, simpleOutputFile)
# Intcoder.run_Intcode_with_input(1)

#simpleInput_opcode2 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
#simpleOutputFile = "output_programcodes.txt"
#Intcoder = IntCode(simpleInput_opcode2, simpleOutputFile)
#Intcoder.run_Intcode_with_input(8)
#output == 1000

#simpleInput_opcode2 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, 1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
#simpleOutputFile = "output_programcodes.txt"
#Intcoder = IntCode(simpleInput_opcode2, simpleOutputFile)
#Intcoder.run_Intcode_with_input(8)
#output == 1000

jmp_test_posmode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
jmp_test_immediate_mode = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
OutputFile = "output_programcodes.txt"
Intcoder = IntCode(jmp_test_immediate_mode)
Intcoder.run_Intcode_with_input(0)

Input_day5 = "Day_5_input.txt"
OutputFile = "output_programcodes.txt"
Intcoder = IntCode(Input_day5)
Intcoder.run_Intcode_with_input(5)
#result 13758663
