import re

def task1(filename: str) -> int:
    input = open(filename)

    pattern = r"[&/%*$+=@#-]"
    
    matches = []
    output = 0
    nums = {}
    for count_line, line in enumerate(input, start=1):
        x = re.finditer(r"\d+", line)
        for el in x:
            matches.append([el.span(), el.group()])
        nums[count_line] = matches.copy()
        matches.clear()

    input.close()
    
    input = open(filename)

    for count, line in enumerate(input, start=1):
        for elem in re.finditer(pattern, line):
            for index in [-1,0,1]:
                for e1 in nums[count + index]:
                    if elem.start() - 1 < e1[0][1] and elem.end() + 1 > e1[0][0]:
                        output += int(e1[1])

    print(output)


def task2(filename: str) -> int:

    input = open(filename)

    pattern = r"[*]"

    matches = []
    output = 0
    nums = {}

    for count_line, line in enumerate(input, start=1):
        x = re.finditer(r"\d+", line)
        for el in x:
            matches.append([el.span(), el.group()])
        nums[count_line] = matches.copy()
        matches.clear()
    
    input.close()
    
    input = open(filename)

    r = 1
    licz = 0

    for count, line in enumerate(input, start=1):
        for elem in re.finditer(pattern, line):
            for index in [-1,0,1]:
                for e1 in nums[count + index]:
                    if elem.start() - 1 < e1[0][1] and elem.end() + 1 > e1[0][0]:
                        r *= int(e1[1])
                        licz +=1
        if licz == 2:
            output += r
        
        r = 1
        licz = 0

    print(output)
    

def main():
    #task1("input1.txt")
    task2("input2.txt")

if __name__ == "__main__":
    main()