import re

input = open("input2.2.txt")

result = 0

for line in input:
    line = line.strip()

    power = 1

    dictionary = {
    "blue":0,
    "red":0,
    "green":0
}

    splitted_line = line.split(":", 1)
    game = splitted_line[0].split()[1]
    data = splitted_line[1]

    cubes = re.split("[,;]", data)

    
    for cube in cubes:
        cube = cube.split()
        if cube[1] in dictionary and int(dictionary[cube[1]]) < int(cube[0]):
            dictionary[cube[1]] = cube[0]
    
    for elem in dictionary.values():
        power = power * int(elem)
    

    result += power
    

print(result)