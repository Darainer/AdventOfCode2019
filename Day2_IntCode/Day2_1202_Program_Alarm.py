from IntCode import IntCode
import pickle


#### instances

def find_inputs_for_computeResult(intcoder: IntCode, inputRangemin, inputRangemax, computeResult) -> int:
    for input1 in range(inputRangemin, inputRangemax, 1):
        for input2 in range(inputRangemin, inputRangemax, 1):
            result = compute_with_changed_inputs(intcoder, input1, input2)
            if result == computeResult:
                print("noun", input1, "verb", input2, "100*noun + verb ", (100 * input1 + input2))
                return (100 * input1 + input2)
            else:
                intcoder.reset()


def compute_with_changed_inputs(intcoder: IntCode, input1, input2) -> int:
    intcoder.program_codes[1] = input1
    intcoder.program_codes[2] = input2
    intcoder.compute_program()
    return intcoder.program_codes[0]


def main():
    simpleInput = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    simpleOutputFile = "output_simple_programcodes.txt"
    Intcoder = IntCode(simpleInput, simpleOutputFile)
    Intcoder.write_output()

    ##

    simpleInput2 = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    simpleOutputFile2 = "output_simple_programcodes2.txt"
    # test2 = tuple(simpleInput2, simpleOutputFile2)
    Intcoder = IntCode(simpleInput2, simpleOutputFile2)
    Intcoder.write_output()

    test_in3 = [2, 4, 4, 5, 99, 0]
    Inttest3 = IntCode(test_in3, "test3_out")
    testOut3 = [2, 4, 4, 5, 99, 9801]

    # parse input file into operational lines
    RealinputFile = "Real_program_codes.txt"
    RealoutputFile = "1202_Program_output.txt"
    Intcoder_real = IntCode(RealinputFile, RealoutputFile)
    Intcoder_real.write_output()

    IntCoder_part2 = IntCode(RealinputFile)
    result_part2 = find_inputs_for_computeResult(IntCoder_part2, 0, 99, 19690720)
    print("result_part2", result_part2)


if __name__ == "__main__":
    main()
