#6. Mobilization

def writeFile(result_arr):
    outFile = open('output.txt', 'w')
    for result in result_arr:
        outFile.write("%d\n" % result)
    outFile.close()

def getAnswer(size, first_arr, second_arr):
    razn_arr = dict()
    for i in range(size):
        razn_arr[first_arr[i] - second_arr[i]] = second_arr[i]
    result = 0
    for i,key in enumerate(sorted(razn_arr.keys())):
        if i >= size/2:
            result += razn_arr[key] + key
        else:
            result += razn_arr[key]
    return result

def readFile():
    first_arr = []
    second_arr = []
    certif_arr = []
    with open("input.txt") as inFile:
        size = int(inFile.readline())
        for x in inFile.readline().split():
            first_arr.append(int(x)) 
        for x in inFile.readline().split():
            second_arr.append(int(x))
        #second_arr = inFile.readline().split()
        count = int(inFile.readline())
        for line in inFile:
        	certif_arr.append([int(x) for x in line.split()])
    return size, first_arr, second_arr, count, certif_arr

def main():
    size, first_arr, second_arr, count, certif_arr = readFile()
    result_arr = []
    for val in certif_arr:
        if val[1] == 1:
            first_arr[val[0] - 1] += val[2]
        else:
            second_arr[val[0] - 1] += val[2]
        result_arr.append(getAnswer(size, first_arr, second_arr))
    writeFile(result_arr)

if __name__ == '__main__':
    main()
