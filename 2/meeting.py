#2. Meeting
import re

def printPoint(data, printList):
    outFile = open('output.txt', 'w')
    for value in data:
        if (value[-1] == "OK"):
            outFile.write("OK\n")
        if (value[-1] == "FAIL"):
            outFile.write("FAIL\n")
            for x in value[6:-3]:
                outFile.write("%s " % x)
            outFile.write("\n")
    for i in printList:
        for j in data:
            if ((i[1] == j[1]) and (j.count(i[2]) > 0)):
                outFile.write("%s:%s %s " % (j[2], j[3], j[4]))
                for x in j[6:-3]:
                    outFile.write("%s " % x)
                outFile.write("\n")
                break
    outFile.close()

def addPoint(data):
    checkList = []
    for values in data:
        values.append(int(int(values[1])*60*24 + int(values[2])*60 + int(values[3])))
        values.append(int(int(values[-1]) + int(values[4])))
        if (len(checkList) == 0):
            values.append("OK")
        else:
            for line in checkList:
                if line[-1] == 'OK':
                    if ((values[-2] >= line[-3] and values[-2] < line[-2]) or (values[-1] > line[-3] and values[-1] <= line[-2])):
                        values.append("FAIL")
                        break
                    else:
                        values.append("OK")
                        break 
        checkList.append(values)
    return data

def readFile():
    data = []
    with open("input.txt") as inFile:
        size = int(inFile.readline())
        for line in inFile:
            data.append(re.findall(r"[\w']+", line))
    return size, data


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