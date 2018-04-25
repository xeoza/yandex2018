#1.Error

def bayesRule(data):
    result = []
    summ = 0
    for values in data:
        values[0] = values[0] * values[1]
        summ += values[0]
    for values in data:
        result.append(values[0]/summ)
    return result

def readFile():
    data = []
    with open("input.txt") as inFile:
        size = int(inFile.readline())
        for line in inFile:
            data.append([int(x) for x in line.split()])
    return size, data

def writeFile(result):
    outFile = open('output.txt', 'w')
    for value in result:
        outFile.write("%.12f\n" % value)
    outFile.close()

def main():
    size, data = readFile()
    result = bayesRule(data)
    writeFile(result)

if __name__ == '__main__':
	main()
