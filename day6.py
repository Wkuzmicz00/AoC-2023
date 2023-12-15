import re
import math

def ceil(number) -> int:
    if number == math.ceil(number):
        number +=1

    return math.ceil(number)

def floor(number) -> int:
    if number == math.floor(number):
        number -=1

    return math.floor(number)



def task1(filename: str) -> int:
    input = open(filename)

    times = re.findall(r'\d+', input.readline())
    distances = re.findall(r'\d+', input.readline())

    numberOfWaysToWin = []

    output = 1

    for time, distance in zip(times, distances):

        #-x^2 + time*x - distance > 0
        time = int(time)
        distance = int(distance)
        deltaSqrt = math.sqrt(pow(time, 2) - (4*-1*-distance))
        x1 = (-time + deltaSqrt)/(-2)
        x2 = (-time - deltaSqrt)/(-2)

        numberOfWaysToWin.append(floor(x2) - ceil(x1) + 1)

    for number in numberOfWaysToWin:
        output *= number

    return output


def task2(filename: str) -> int:

    input = open(filename)

    times = re.findall(r'\d+', input.readline())
    distances = re.findall(r'\d+', input.readline())
    
    time = ""
    distance = ""

    for t, d in zip(times, distances):
        time += t
        distance += d

    time = int(time)
    distance = int(distance)
    deltaSqrt = math.sqrt(pow(time, 2) - (4*-1*-distance))
    x1 = (-time + deltaSqrt)/(-2)
    x2 = (-time - deltaSqrt)/(-2)

    output = floor(x2) - ceil(x1) + 1
    return(output)




def main() -> None:
    print(task1("input2.txt"))
    print(task2("input2.txt"))

if __name__ == "__main__":
    main()