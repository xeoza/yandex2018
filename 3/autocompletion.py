#3. Autocompletion

def findSuggestions(words, prefix):

    prefixLength = len(prefix)
    index = findIndex(words, prefix, prefixLength, 0, len(words))

    if index == -1:
      return []

    first = index
    while first > 0 and words[first-1][:prefixLength] == prefix:
      first -= 1

    last = index
    while last < len(words)-1 and words[last+1][:prefixLength] == prefix:
      last += 1  
    
    return words[first:last + 1]

def findIndex(words, prefix, prefixLength, start, end):
    if start >= end:
      return -1 

    middle = int((end - start)/2) + start
    checkWordPrefix = words[middle][:prefixLength]
    if prefix < checkWordPrefix:
        return findIndex(words, prefix, prefixLength, start, middle)
    elif prefix > checkWordPrefix:
        return findIndex(words, prefix, prefixLength, middle+1, end)
    else:
        return middle

def writeFile(result):
    outFile = open('output.txt', 'w')
    outFile.write("%d" % result)
    outFile.close()

def readFile():
    data = []
    with open("input.txt") as inFile:
        size = int(inFile.readline())
        data = inFile.read().split()
    return size, data

def main():
    size, data = readFile()
    word = ''
    answer = 0
    dictionary = []
    for value in data:
        for i in value:
            
            word += i
            arr = findSuggestions(dictionary, word)

            if not arr or (len(arr) == 1 and arr[0] != value):
                dictionary.append(value)
                answer += len(value)
                break

            if (len(arr) == 1 and arr[0] == value) or len(value) == 1:
                answer += len(word)
                break 
        word = ''

    writeFile(answer)

if __name__ == '__main__':
    main()