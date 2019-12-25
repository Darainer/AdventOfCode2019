# intcode computer

def split_int_to_list(int_number: int) -> list:
    digit_list = []
    while int_number > 0:
        digit_list.append(int_number % 10)
        int_number //= 10
    digit_list.reverse()
    return digit_list

class IntCode:
    def __init__(self, input_code, output_file):
        if type(input_code) is str:
            self.read_program_txt(input_code)
        else: #input is a list of ints
            self.program_codes = input_code
        self.original_codes = list(self.program_codes) # make an initial copy
        self.output_file = output_file
        self.input = -1
        self.output = -1


    def run_Intcode_with_input(self,input_int: int):
        self.input = input_int
        self.compute_program()

    def read_program_txt(self, input_file):
        with open(input_file, 'r') as file:
            program_input = file.readline()
            program_codes = program_input.split(',')
            self.program_codes = [int(i) for i in program_codes]

    def find_inputs_for_computeResult(self,inputRangemin,inputRangemax,computeResult):
        for input1 in range(inputRangemin, inputRangemax, 1):
            for input2 in range(inputRangemin, inputRangemax, 1):
                result = self.compute_with_changed_inputs(input1, input2)
                if result == computeResult:
                    print("noun", input1, "verb", input2, "100*noun + verb ", (100*input1+input2))
                    return 0
                else:
                    self.program_codes = list(self.original_codes)

    def compute_with_changed_inputs(self, input1, input2) -> int:
        self.program_codes[1] = input1
        self.program_codes[2] = input2
        self.compute_program()
        return self.program_codes[0]


    def compute_program(self) -> bool:
        idx = 0
        while idx <= len(self.program_codes):
            #print(idx)  #for debug
            program_code_list = split_int_to_list(self.program_codes[idx])
            if program_code_list[-1] == 1:                              # Addition
                self.intcode_operation_1(idx,program_code_list)
                idx = idx + 4
            elif program_code_list[-1] == 2:                            # Multiplication
                self.intcode_operation_2(idx,program_code_list)
                idx = idx + 4
            elif program_code_list[-1] == 3:                            # input
                self.intcode_operation_3(idx, self.input)
                idx = idx + 2
            elif program_code_list[-1] == 4:                            # return
                self.intcode_operation_4(idx, program_code_list)
                idx = idx + 2
            elif program_code_list[-1] == 5:                            # jmp if True
                idx = self.intcode_operation_5(idx, program_code_list)
            elif program_code_list[-1] == 6:                            # jmp if False
                idx = self.intcode_operation_6(idx, program_code_list)
            elif program_code_list[-1] == 7:                            # compare
                self.intcode_operation_7(idx,program_code_list)
                idx = idx + 4
            elif program_code_list[-1] == 8:                            # is Equal
                self.intcode_operation_8(idx,program_code_list)
                idx = idx + 4
            elif program_code_list[-1] and program_code_list[-2] == 9:  # code 99 program finish
                return True
            else:
                return False

    def get_op_arguments(self, index, program_code_list: list) -> list:
        #can be just a single opcode if others are all leading zeros
        arg_2 = 0
        opmode_param1 = opmode_param2 = 0
        if len(program_code_list)>=3:
            opmode_param1 = program_code_list[-3]
        if len(program_code_list)>=4:
            opmode_param2 = program_code_list[-4]
        if opmode_param1 == 0:
            idx_m1 = self.program_codes[index + 1]
            arg_1 = self.program_codes[idx_m1]
        elif opmode_param1 ==1:
            arg_1 = self.program_codes[index + 1]
        if opmode_param2 == 0 and (program_code_list[-1] != 4):
            idx_m2 = self.program_codes[index + 2]
            arg_2 = self.program_codes[idx_m2]
        elif opmode_param2 ==1:
            arg_2 = self.program_codes[index + 2]
        return [arg_1, arg_2]

    def intcode_operation_1(self, index, program_code_list: list) -> bool:  #addition
        [arg1, arg2] =self.get_op_arguments(index, program_code_list)
        idx_result = self.program_codes[index + 3]
        self.program_codes[idx_result] = arg1 + arg2

    def intcode_operation_2(self, index, program_code_list: list)-> bool:  #multiplication
        [arg1, arg2] = self.get_op_arguments(index, program_code_list)
        idx_mresult = self.program_codes[index + 3]
        self.program_codes[idx_mresult] = arg1 * arg2

    def intcode_operation_3(self, index, input: int):  # save value
        idx_result = self.program_codes[index + 1]
        self.program_codes[idx_result] = input

    def intcode_operation_4(self, index,program_code_list: list):            # retrieve value
        [arg1, arg2] = self.get_op_arguments(index, program_code_list)
        self.output = arg1
        print("diagnostic result", self.output)

    def intcode_operation_5(self,index, program_code_list: list)->int:           # jump if Nonzero
        [arg1, arg2] = self.get_op_arguments(index, program_code_list)
        if arg1 != 0:
            idx = arg2
        else:
            idx = index + 3
        return idx

    def intcode_operation_6(self, index, program_code_list: list)->int:           # jump if False
        [arg1, arg2] = self.get_op_arguments(index, program_code_list)
        if arg1 == 0:
            idx = arg2
        else:
            idx = index + 3
        return idx

    def intcode_operation_7(self, index, program_code_list: list) -> bool:  #less than
        [arg1, arg2] =self.get_op_arguments(index, program_code_list)
        idx_result = self.program_codes[index + 3]
        if arg1 < arg2:
            self.program_codes[idx_result] = 1
        else:
            self.program_codes[idx_result] = 0

    def intcode_operation_8(self, index, program_code_list: list)-> bool:  # is equals
        [arg1, arg2] = self.get_op_arguments(index, program_code_list)
        idx_result = self.program_codes[index + 3]
        if arg1 == arg2:
            self.program_codes[idx_result] = 1
        else:
            self.program_codes[idx_result] = 0

# todo: tests for all intcode puzzles, can prob delete this
    def write_output(self):
        f = open(self.output_file, 'w')
        output_list = [str(i) for i in self.program_codes]
        for i in range(len(output_list)):
            f.write(output_list[i])
            if i != len(output_list)-1:
                f.write(",")
        f.close()

    def __del__(self):
        print('Destructor called, Instance deleted.')
