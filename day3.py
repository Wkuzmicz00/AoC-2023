import re

def task1(filename: str) -> int:
    input = open(filename)


    pattern = r"[&/%*$+=@#-]"
    
    matches = []
    sum = 0
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
                        sum += int(e1[1])

    print(sum)

    
     









def main():
    task1("input1.txt")

if __name__ == "__main__":
    main()