from IntCode import IntCode
import itertools

# Here are some example programs:
#
#     Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):
#
#     3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
#
#     Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):
#
#     3,23,3,24,1002,24,10,24,1002,23,-1,23,
#     101,5,23,23,1,24,23,23,4,23,99,0,0
#
#     Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):
#
#     3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
#     1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
#input_program = 'Day7_AMP_input_program.txt'

input_program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
Amplist = []
phase_codes = [0,1,2,3,4]
Phase_Combinations = [",".join(map(str, comb)) for comb in itertools.combinations(phase_codes, 5)]
Phase_per = [",".join(map(str, comb)) for comb in itertools.permutations(phase_codes, 5)]
Phase_per2 = [list.append((*comb)) for comb in itertools.permutations(phase_codes, 5)]

#itertools.permutations(iterable[, r])
Phase_Permutations = []
#p = itertools.permutations(phase_codes[, 5])

i = 0
for permutation in itertools.permutations(phase_codes):
    Phase_Permutations[i] = permutation
    i += 1

#phase_codes.
i = 0
while i <= 4:
    Amplist.append(IntCode(input_program))
    i += 1

input = 0
for i in Amplist:
    #todo get intcode to accept programs with second input
    Amplist[i].run_Intcode_with_input(0)
print(Amplist[0].output)
