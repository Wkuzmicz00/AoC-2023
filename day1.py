
input = open("input1.txt", "r")

result = 0

for line in input:

    i = 0
    j = -1
    left = None
    right = None

    while left is None:
        if line.strip()[i].isdigit():
            left = line.strip()[i]
            break
        i += 1
    
    while right is None:
        if line.strip()[j].isdigit():
            right = line.strip()[j]
            break
        j -= 1
        
    
    result += ((int(left) * 10) + int(right))
    print(result)




    
