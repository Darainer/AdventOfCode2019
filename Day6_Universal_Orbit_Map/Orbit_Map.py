def check_depth(List_of_orbits, planet):
    count = 0
    while planet in List_of_orbits:
        count += 1
        planet = List_of_orbits[planet]
    return count

#input_file = "test_inputs.txt"
input_file = "Input_Orbits.txt"
List_of_orbits = {}

with open(input_file, 'r') as file:
    for lines in file:
        l = lines.strip('\n')
        [orbit_pair1, orbit_pair2] = l.split(')')
        List_of_orbits[orbit_pair2] = orbit_pair1

total_orbits = 0
for planet in List_of_orbits.keys():
    orbits = check_depth(List_of_orbits, planet)
    total_orbits += orbits

print(total_orbits)