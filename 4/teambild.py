'''
3 1
1 2
'''
def getAnswer(size, rebro, data):
    for i, key in enumerate(sorted(data.keys())):
        for j in data.get(key):
            if key == j :
                data[key].append(j)
                print('OK',j, data[key])
            print(key, j)

def writeFile(result):
    outFile = open('output.txt', 'w')
    #outFile.write("%d" % result)
    outFile.close()

def readFile():
    data = dict()
    with open("input.txt") as inFile:
        size, rebro = inFile.readline().split()
        for line in inFile:
            data[int(line[0])] = [int(line[2])]
    return size, rebro, data

def main():
    size, rebro , data = readFile()
    resultArr = getAnswer(size, rebro, data)
    print(size,rebro,data)
    

if __name__ == '__main__':
    main()