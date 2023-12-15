
def task1(file: str) -> int:
    input = open("input1.txt", "r")

    output = 0

    for line in input:
        i = 0
        j = -1
        
        left, right = None

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
    
        output += ((int(left) * 10) + int(right))
    return output

def task2(file: str) -> int:
    input = open("input1.1.txt", "r")

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
    
    return output

def main() -> None:
    output1 = task1("input.txt")
    output2 = task2("input2.txt")
    print(output1, output2)

if __name__ == "__main__":
    main()
    







    
