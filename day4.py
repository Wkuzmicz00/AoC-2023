import re

def task1(fileName: str) -> int:
    input = open(fileName)

    output = 0
    winnings = 0

    for line in input:
        numbers = re.findall(r"\d+", line)
        winningNumbers, myNumbers = numbers[1:11], numbers[11:]

        for number in myNumbers:
            if number in winningNumbers:
                winnings +=1
        
        if winnings > 0:
            output += pow(2, winnings-1)
            winnings = 0
        

    return(output)

def task2(fileName: str) -> int:
    with open(fileName, 'r') as file:
        lines = file.readlines()

    output = 0
    winnings = 0

    copys = [1] * len(lines)

    for currentCard, line in enumerate(lines, start=0):
        numbers = re.findall(r"\d+", line)
        winningNumbers, myNumbers = numbers[1:11], numbers[11:]

        for number in myNumbers:
            if number in winningNumbers:
                winnings += 1
        
        for i in range(winnings):
            if i + currentCard <= len(lines)-1:
                copys[currentCard + (i+1)] += 1 * copys[currentCard]
        
        output += 1 * copys[currentCard]
        
        winnings = 0
        
    return(output)




def main() -> None:
    print("task1: ", task1("input2.txt"))
    print("task2: ", task2("input2.txt"))

if __name__ == "__main__":
    main()