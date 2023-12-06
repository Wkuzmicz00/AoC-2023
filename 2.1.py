import re

input = open("input2.1.txt")

dictionary = {
    "red":12,
    "green":13,
    "blue":14
}

result = 0

for line in input:
    line = line.strip()

    splitted_line = line.split(":", 1)
    game = splitted_line[0].split()[1]
    print(game)
    data = splitted_line[1]

    cubes = re.split("[,;]", data)

    gameIsPossible = True
    
    for cube in cubes:
        cube = cube.split()
        if int(cube[0]) > dictionary[cube[1]]:
            gameIsPossible = False
    
    if gameIsPossible:
        result += int(game)

print(result)


 