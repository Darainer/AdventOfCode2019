
def calculatefuel(module_mass):
#    fuel required for a module, take its mass, divide by three, round down, and subtract 2.
    fuel = (module_mass / 3)
    return fuel

def CalculateModuleFuel(fuelslice):
    Modulefuel = 0
    while calculatefuel(fuelslice) >=0:
        fuelslice = calculatefuel(fuelslice)
        Modulefuel += fuelslice
    return Modulefuel

def CalculateFuelForInputModuleTxt(inputFile):
    f = open(inputFile, "r")
    TotalFuel = 0
    for TextLine in f:
        ModuleFuel = CalculateModuleFuel(int(TextLine))
        TotalFuel += ModuleFuel
    print('For ALL Spaceship modules', TotalFuel)
    return TotalFuel

ModuleFuel = CalculateModuleFuel(1969)
print('For module of Mass', 1969,  'fuel needed', ModuleFuel)

TotalFuel = CalculateFuelForInputModuleTxt("InputModules.txt")







