input = open("input1.1.txt")

dictionary = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

keywords = list(dictionary.keys())

output = 0

for line in input:

    line = line.strip()

    right = None
    left = None
    i = 0
    j = -1

    while left is None:
        if line[i].isdigit():
            left = line[i]
            break
        else:
            i += 1
            for keyword in keywords:
                if keyword in line[:i]:
                    left = dictionary[keyword]
                    break
    
    while right is None:
        if line[j].isdigit():
            right = line[j]
            break
        else:
            for keyword in keywords:
                if keyword in line[j:]:
                    right = dictionary[keyword]
                    break
        j -= 1
    
    output += ((int(left) * 10)+int(right))
    

print(output)

    



    
        



