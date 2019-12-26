def get_full_depth(List_of_orbits, planet):
    count = 0
    while planet in List_of_orbits:
        count += 1
        planet = List_of_orbits[planet]
    return count

def get_full_list_of_parents(List_of_orbits, planet):
    count = 0
    planet_dict = {}
    while planet in List_of_orbits:
        count += 1
        planet = List_of_orbits[planet]
        planet_dict[planet] = count
    return planet_dict

def transfers_to_target_planet(List_of_orbits, planet, target_planet):
    transfers_needed = 0
    while List_of_orbits[planet] != target_planet:
        transfers_needed += 1
        planet = List_of_orbits[planet]
    return transfers_needed

#input_file = "test_inputs.txt"
#input_file = "test6b.txt"
input_file = "Input_Orbits.txt"
List_of_orbits = {}

with open(input_file, 'r') as file:
    for lines in file:
        l = lines.strip('\n')
        [orbit_pair1, orbit_pair2] = l.split(')')
        List_of_orbits[orbit_pair2] = orbit_pair1

total_orbits = 0
for planet in List_of_orbits.keys():
    orbits = get_full_depth(List_of_orbits, planet)
    total_orbits += orbits

print("Part1: total direct and indirect orbits", total_orbits)

#part2
santa_orbit_list = get_full_list_of_parents(List_of_orbits, "SAN")
my_orbit_list = get_full_list_of_parents(List_of_orbits, "YOU")
my_sorted_orbits = sorted(my_orbit_list.items(), key=lambda x: x[1])

for my_orbiter in my_sorted_orbits:
    if my_orbiter[0] in santa_orbit_list:
        common_planet = my_orbiter[0]
        break

if common_planet:
    transfers_me_to_common_planet = transfers_to_target_planet(List_of_orbits, "YOU", common_planet)
    transfers_santa_to_common_planet = transfers_to_target_planet(List_of_orbits, "SAN", common_planet)
    total_transfers = transfers_me_to_common_planet + transfers_santa_to_common_planet

print("Part2: total transfers needed",total_transfers)
