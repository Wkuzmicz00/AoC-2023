import re

def task1(filename: str) -> int:
    input = open(filename, "r")
    output = 0

    seeds = re.findall(r"\d+", input.readline())

    input.readline()

    unparsedMaps = ["", "", "", "", "", "", "", ""] 
    maps = []
    i = 0

    for line in input:
        unparsedMaps[i] += line
        if line == "\n":
            i += 1
    
    for map in unparsedMaps:
        maps.append(re.findall(r"\d+", map))

    j = 0
    i = 0

    locations = []

    for seed in seeds:
        current = int(seed)

        i = 0
        while i < 7:
            j = 0
            while ((j/3)+1) <= len(maps[i])/3:
                if int(maps[i][1+j]) <= current and int(maps[i][1+j]) + int(maps[i][2+j]) - 1 >= current:
                    current = (current - int(maps[i][1+j])) + int(maps[i][j])
                    break
                j += 3
            i += 1
        
        locations.append(current)

    output = min(locations)
        
    return(output)



def main() -> None:
    print(task1("input2.txt"))

if __name__ == "__main__":
    main()

