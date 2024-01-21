#Class to print numbers, with string substitutes for
#numbers that are divisible by passed in factors
class NumberPrinter:
    
    def printNumbers(self, n: int, numStrMap: dict):
        for i in range(1, n+1):
            output = []
            for key in numStrMap:
                if i % key == 0:
                    output.append(numStrMap[key])
            output = output or [str(i)]
            print(''.join(output))
           
numStrMap = {3: "Crackle", 5: "Pop"}
numPrinter = NumberPrinter()
numPrinter.printNumbers(100, numStrMap)

