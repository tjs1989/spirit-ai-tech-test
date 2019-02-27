numberRange = 100
firstFibNum = 0
secondFibNum = 1
fibonacciList = []

while secondFibNum < numberRange:
    fibonacciList.append(secondFibNum)
    firstFibNum, secondFibNum = secondFibNum, firstFibNum + secondFibNum

def checkIfNumberIsMoreThanOneMultiple(number,singleMultipleResponse):
    if (number % 3 == 0) and (number % 5 == 0) and fibonacciList.count(number) > 0:
        return "PinkFlamingo"
    elif (number % 3 == 0) and (number % 5 == 0):
        return "FizzBuzz"
    else: return singleMultipleResponse

for number in range(numberRange):
    number = number + 1
    if (number % 3 == 0):
        print checkIfNumberIsMoreThanOneMultiple(number,"Fizz")
    elif (number % 5 == 0):
        print checkIfNumberIsMoreThanOneMultiple(number,"Buzz")
    elif   fibonacciList.count(number) > 0:
        print checkIfNumberIsMoreThanOneMultiple(number,"Flamingo")
    else: print number