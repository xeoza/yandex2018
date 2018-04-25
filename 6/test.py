#6. Mobilization
import random
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
    middle = size/2
    for i,key in enumerate(sorted(razn_arr.keys())):
        if i >= middle:
            result += razn_arr[key] + key
        else:
            result += razn_arr[key]
    return result

def readFile():
    first_arr = []
    second_arr = []
    certif_arr = []
    with open("test.txt") as inFile:
        size = int(inFile.readline())
        for x in inFile.readline().split():
            first_arr.append(int(x)) #= inFile.readline().split()
        for x in inFile.readline().split():
            second_arr.append(int(x))
        #second_arr = inFile.readline().split()
        count = int(inFile.readline())
        for line in inFile:
        	certif_arr.append([int(x) for x in line.split()])
    return size, first_arr, second_arr, count, certif_arr

def main():
    #size, first_arr, second_arr, count, certif_arr = readFile()
    '''size = 100000
    first_arr = []
    second_arr = []
    count = 100
    certif_arr = [[1, 1, 1000]]
    for i in range(2*size):
        first_arr.append(random.randint(0, 1000000000))
        second_arr.append(random.randint(0, 1000000000))
    for i in range(count):
        certif_arr.append([random.randint(1, 2*size),random.randint(1, 2), random.randint(1, 10000)])
    '''
    result_arr = []
    '''
    with open("test.txt", "w") as outFile:
        outFile.write("%d\n" % size)
        for val in first_arr:
            outFile.write("%d " % val)
        outFile.write("\n")
        for val in second_arr:
            outFile.write("%d " % val)
        outFile.write("\n%d\n" % count)
        for val in certif_arr:
            outFile.write("%d %d %d\n" % (val[0], val[1], val[2]))
    '''
    first_arr = []
    second_arr = []
    certif_arr = []
    outFile = open('output.txt', 'w')
    with open("test.txt") as inFile:
        size = int(inFile.readline())
        #line1 = inFile.readline().split()
        #line2 = inFile.readline().split() 
        for f_val, s_val in zip(inFile.readline().split(), inFile.readline().split()):
        #first_arr = list(map(int, inFile.readline().split()))
        #print(first_arr)
            first_arr.append(int(f_val)) #= inFile.readline().split()
        #for x in inFile.readline().split():
        #second_arr = list(map(int, inFile.readline().split()))
            second_arr.append(int(s_val))
        #second_arr = inFile.readline().split()
        count = int(inFile.readline())
        razn_arr = dict()
        result_arr = []
        for line in inFile:
            for x in line.split():
                certif_arr.append(int(x))
            if certif_arr[1] == 1:
                first_arr[certif_arr[0] - 1] += certif_arr[2]
            else:
                second_arr[certif_arr[0] - 1] += certif_arr[2]
            certif_arr.clear()
            for i in range(size):
                razn_arr[first_arr[i] - second_arr[i]] = second_arr[i]
            result = 0
            middle = size/2
            for i,key in enumerate(sorted(razn_arr.keys())):
                if i >= middle:
                    result += razn_arr[key] + key
                else:
                    result += razn_arr[key]
            outFile.write("%d\n" % result)
        outFile.close()

'''    for val in certif_arr:
        if val[1] == 1:
            first_arr[val[0] - 1] += val[2]
        else:
            second_arr[val[0] - 1] += val[2]'''
        #result_arr.append(getAnswer(size, first_arr, second_arr))
    #writeFile(result_arr)

if __name__ == '__main__':
    main()
