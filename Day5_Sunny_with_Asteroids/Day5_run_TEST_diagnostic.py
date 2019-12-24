from IntCode import IntCode

simpleInput_opcode3 = [3,0,4,0,99]
simpleOutputFile = "output_simple_programcodes.txt"
Intcoder = IntCode(simpleInput_opcode3, simpleOutputFile)
output = Intcoder.run_Intcode_with_input_output(43)
print(output)

#Intcoder.write_output()
