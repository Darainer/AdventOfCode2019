# intcode computer
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


    def run_Intcode_with_input_output(self,input_int: int)->int:
        self.input = input_int
        self.compute_program()
        return self.output

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
            if self.program_codes[idx] == 1:
                self.intcode_operation_1(idx)
                idx = idx + 4
            elif self.program_codes[idx] == 2:
                self.intcode_operation_2(idx)
                idx = idx + 4
            elif self.program_codes[idx] == 3:
                self.intcode_operation_3(idx, self.input)
                idx = idx + 2
            elif self.program_codes[idx] == 4:
                self.intcode_operation_4(idx)
                idx = idx + 2
            elif self.program_codes[idx] == 99:  # program finish
                return True
            else:
                return False

    def intcode_operation_1(self, index) -> bool:  #addition
        idx_1 = self.program_codes[index+1]
        idx_2 = self.program_codes[index+2]
        idx_result = self.program_codes[index + 3]
        self.program_codes[idx_result] = self.program_codes[idx_1] + self.program_codes[idx_2]

    def intcode_operation_2(self, index)-> bool:  #multiplication
        idx_m1 = self.program_codes[index + 1]
        idx_m2 = self.program_codes[index + 2]
        idx_mresult = self.program_codes[index + 3]
        self.program_codes[idx_mresult] = self.program_codes[idx_m1] * self.program_codes[idx_m2]

    def intcode_operation_3(self,index, input :int):  # save value
        idx_1 = self.program_codes[index + 1]
        self.program_codes[idx_1] = input

    def intcode_operation_4(self,index):            # retrieve value
        idx_1 = self.program_codes[index + 1]
        self.output = self.program_codes[idx_1]

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
