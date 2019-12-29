from IntCode import IntCode
import itertools

def CalculateMaxAmplification(inputprogram,phase_codes)->int:
    Amplist = []
    for it in phase_codes:
        Amplist.append(IntCode(inputprogram))

    i = 0
    TotalAmplification = []
    ThrusterOutput = 0

    Phase_code_permutations = list(itertools.permutations(phase_codes))
    for permutation in Phase_code_permutations:
        for Amplifier in Amplist:
            ThrusterOutput = Amplifier.run_Intcode_with_input_output([permutation[i], ThrusterOutput])
            i += 1
        TotalAmplification.append([ThrusterOutput, permutation])
        i = 0
        ThrusterOutput = 0
    TotalAmplification.sort(key=lambda x: x[0], reverse=True)
    return TotalAmplification[0][0]

def resetAmplifiers(Amplist):
    for Amplifier in Amplist:
        Amplifier.reset()

def FeedbackAmplification(inputprogram,phase_codes)->int:
    Amplist = []
    for it in phase_codes:
        Amplist.append(IntCode(inputprogram))
        Amplist[-1].setFeedbackmode(True)

    TotalAmplification = []
    ThrusterOutput = 0
    Phase_code_permutations = list(itertools.permutations(phase_codes))
    for permutation in Phase_code_permutations:
        i = 0
        for Amplifier in Amplist:
            ThrusterOutput = Amplifier.run_Intcode_with_input_output([permutation[i], ThrusterOutput])
            i+=1
        while Amplist[-1].isIntcodeActive():
            for Amplifier in Amplist:
                ThrusterOutput = Amplifier.run_Intcode_with_input_output([ThrusterOutput])
        TotalAmplification.append([ThrusterOutput, permutation])
        ThrusterOutput = 0
        resetAmplifiers(Amplist)

    TotalAmplification.sort(key=lambda x: x[0], reverse=True)
    return TotalAmplification[0][0]
