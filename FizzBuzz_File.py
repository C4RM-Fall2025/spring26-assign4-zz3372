def FizzBuzz(start, finish):
    outList = []
    for n in range(start, finish + 1):
        if n % 15 == 0:
            outList.append("fizzbuzz")
        elif n % 3 == 0:
            outList.append("fizz")
        elif n % 5 == 0:
            outList.append("buzz")
        else:
            outList.append(n)
    return (outList)
    
