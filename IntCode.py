# intcode computer

from itertools import repeat


def split_int_to_list(int_number: int) -> list:
    digit_list = []
    while int_number > 0:
        digit_list.append(int_number % 10)
        int_number //= 10
    digit_list.reverse()
    return digit_list

class IntCode:
    def __init__(self, input_code):
        if type(input_code) is str:
            self.read_program_txt(input_code)
        else: #input is a list of ints
            self.program_codes = list(input_code)
        self.append_memory_to_program()
        self.original_codes = list(self.program_codes) # make an initial copy
        #self.output_file = output_file
        self.inputIdx = 0
        self.inputList = []
        self.output = [-1]
        self.isActive = True
        self.feedback_mode = False
        self.program_idx_pointer = 0
        self.relative_base_idx = 0

    def run_Intcode_with_input(self, input):
        if type(input) == int:
            self.inputList.append(input)
        else:
            self.inputList = input
        self.compute_program()

    #todo refactor to not need feedback mode
    def run_Intcode_with_input_output(self, input):
        self.isActive = True
        self.output = [-1]
        if type(input) == int:
            self.inputList.append(input)
        elif self.feedback_mode:
            for i in input:
                self.inputList.append(i)
        else:
            self.inputList = input
        self.compute_program()

        if not self.feedback_mode:
            self.inputIdx = 0

        return self.output

    def setFeedbackmode(self,FeedbackMode:bool):
        self.feedback_mode = FeedbackMode

    def isIntcodeActive(self) -> bool:
        return self.isActive

    def reset(self):
        self.program_codes = list(self.original_codes)
        self.inputIdx = 0
        self.program_idx_pointer = 0
        self.inputList = []
        self.output = [-1]
        self.isActive = True

    def read_program_txt(self, input_file):
        with open(input_file, 'r') as file:
            program_input = file.readline()
            program_codes = program_input.split(',')
            self.program_codes = [int(i) for i in program_codes]

    def append_memory_to_program(self):
        zeros = list(repeat(0, 10000000))
        self.program_codes += zeros

    def compute_program(self) -> bool:
        idx = self.program_idx_pointer
        while idx <= len(self.program_codes):
            print(idx)  #for debug
            program_code_list = split_int_to_list(self.program_codes[idx])
            if program_code_list[-1] == 1:                              # Addition
                self.intcode_operation_1(idx,program_code_list)
                idx += 4
            elif program_code_list[-1] == 2:                            # Multiplication
                self.intcode_operation_2(idx,program_code_list)
                idx += 4
            elif program_code_list[-1] == 3:                            # input
                self.intcode_operation_3(idx, program_code_list, self.inputList[self.inputIdx])
                self.inputIdx += 1
                idx += 2
            elif program_code_list[-1] == 4:                            # return
                self.intcode_operation_4(idx, program_code_list)
                idx += 2
                if self.feedback_mode:
                    self.program_idx_pointer = idx
                    return
            elif program_code_list[-1] == 5:                            # jmp if True
                idx = self.intcode_operation_5(idx, program_code_list)
            elif program_code_list[-1] == 6:                            # jmp if False
                idx = self.intcode_operation_6(idx, program_code_list)
            elif program_code_list[-1] == 7:                            # compare
                self.intcode_operation_7(idx,program_code_list)
                idx += 4
            elif program_code_list[-1] == 8:                            # is Equal
                self.intcode_operation_8(idx,program_code_list)
                idx += 4
            elif program_code_list[-1] ==9:
                if len(program_code_list) >= 2 and program_code_list[-2] == 9:  # code 99 program finish
                    self.isActive = False
                    return
                else:                                                      # shift relative index
                    self.intcode_operation_9(idx, program_code_list)
                    idx += 2

    def get_opcode_arguments(self, instruction_idx, program_code_list: list, no_of_parameters) -> list:
        arglist=[]
        opmodes = [0, 0, 0]  # default to zero (a leading zero is omitted)
        if len(program_code_list) >= 3:
            opmodes[0] = program_code_list[-3]
            if len(program_code_list) >= 4:
                opmodes[1] = program_code_list[-4]
                if len(program_code_list) == 5:
                    opmodes[2] = program_code_list[-5]

        for parameter_int in range(1, no_of_parameters+1):
            if opmodes[parameter_int-1] == 0:                       # position mode
                arg_idx = self.program_codes[instruction_idx + parameter_int]
                arg = self.program_codes[arg_idx]
            elif opmodes[parameter_int-1] == 1:                     # immediate mode
                arg = self.program_codes[instruction_idx + parameter_int]
            elif opmodes[parameter_int-1] == 2:                     # relative mode
                arg_idx = self.program_codes[instruction_idx + parameter_int]
                arg = self.program_codes[self.relative_base_idx + arg_idx]
            arglist.append(arg)
        return arglist

    def intcode_operation_1(self, index, program_code_list: list):  #addition
        [arg1, arg2, arg3] = self.get_opcode_arguments(index, program_code_list, 3)
        self.program_codes[arg3] = arg1 + arg2

    def intcode_operation_2(self, index, program_code_list: list):  #multiplication
        [arg1, arg2, arg3] = self.get_opcode_arguments(index, program_code_list, 3)
        self.program_codes[arg3] = arg1 * arg2

    def intcode_operation_3(self, index, program_code_list: list, input: int):  # save input value
        [arg1] = self.get_opcode_arguments(index, program_code_list, 1)
        self.program_codes[arg1] = input

    def intcode_operation_4(self, index, program_code_list: list):            # retrieve value
        [arg1] = self.get_opcode_arguments(index, program_code_list)
        if self.output[0] == -1:
            self.output[0] = arg1
        else:
            self.output.append(arg1)

    def intcode_operation_5(self, index, program_code_list: list) -> int:           # jump if Nonzero
        [arg1, arg2] = self.get_opcode_arguments(index, program_code_list, 2)
        if arg1 != 0:
            new_idx = arg2
        else:
            new_idx = index + 3
        return new_idx

    def intcode_operation_6(self, index, program_code_list: list) -> int:           # jump if False
        [arg1, arg2] = self.get_opcode_arguments(index, program_code_list, 2)
        if arg1 == 0:
            new_idx = arg2
        else:
            new_idx = index + 3
        return new_idx

    def intcode_operation_7(self, index, program_code_list: list) -> bool:  #less than
        [arg1, arg2, arg3] = self.get_opcode_arguments(index, program_code_list, 3)
        if arg1 < arg2:
            self.program_codes[arg3] = 1
        else:
            self.program_codes[arg3] = 0

    def intcode_operation_8(self, index, program_code_list: list)-> bool:  # is equals
        [arg1, arg2, arg3] = self.get_opcode_arguments(index, program_code_list, 3)
        if arg1 == arg2:
            self.program_codes[arg3] = 1
        else:
            self.program_codes[arg3] = 0

    def intcode_operation_9(self,index, program_code_list: list):
        [arg1] = self.get_opcode_arguments(index, program_code_list, 1)
        self.relative_base_idx += arg1
