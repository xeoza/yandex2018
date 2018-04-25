#2. Meeting
import re

def addPoint(data):
    checkList = dict()
    for values in data:
        okOrFail = True
        for value in values[6:]:
            if value in checkList:
                flagForCheckList = True
                for i in checkList[value]:
                    if values[1] == i[0]:
                        a = int(values[2])*60 + int(values[3])
                        b = a + int(values[4])
                        ai = int(i[1])*60 + int(i[2])
                        bi = ai + int(i[3])
                        if ((ai < a < bi ) or (ai < b < bi)):
                            flagForCheckList = False
                if flagForCheckList:
                    checkList[value].append(values[1:5])
                else:
                    okOrFail = False
            else:
                checkList[value] = [values[1:5]]
        if okOrFail:
            values.append('OK')
        else:
            values.append('FAIL')
    checkList.clear()
    return data

def readFile():
    data = []
    with open("input.txt") as inFile:
        size = int(inFile.readline())
        for line in inFile:
            data.append(re.findall(r"[\w']+", line))
    return size, data


def printPoint(data, printList):
    outFile = open('output.txt', 'w')
    for value in data:
        if (value[-1] == "OK"):
            outFile.write("OK\n")
        if (value[-1] == "FAIL"):
            outFile.write("FAIL\n")
            for x in value[6:-1]:
                outFile.write("%s " % x)
            outFile.write("\n")

    n = 1
    while n < len(data):
        for i in range(len(data)-n):
            if (int(data[i][2])*60 + int(data[i][3])) > (int(data[i+1][2])*60 + int(data[i+1][3])):
                    data[i],data[i+1] = data[i+1],data[i]
        n += 1
    for i in printList:
        for val in data:
            if (i[1] == val[1] and val.count(i[2]) == 1 and val.count('OK') == 1):
                outFile.write("%s:%s %s " % (val[2], val[3], val[4]))
                for x in val[6:-1]:
                    outFile.write("%s " % x)
                outFile.write("\n")

    outFile.close()

def main():
    size, data = readFile()
    appPointList = []
    printList = []
    valid_value = ['APPOINT','PRINT']
    for value in data:
        if (value[0] == valid_value[0]):
            appPointList.append(value)
        if (value[0] == valid_value[1]):
            printList.append(value)
    data = addPoint(appPointList)
    printPoint(data, printList)

if __name__ == '__main__':
    main()