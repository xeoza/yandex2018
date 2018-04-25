def readForDays(numberDays):
    return int((numberDays + 1) * numberDays / 2)

def books(numberDays, k, startDate, m):
    result = 5 * int(numberDays / 7)

    if numberDays % 7 == 0:
        return k * result + m

    end = startDate + numberDays % 7
    result += end - startDate

    if startDate <= 6 and end >= 8:
        result -= 2

    elif startDate == 7 or end == 7:
        result -= 1

    if result > 0:
        return k * result + m

    return m

def f(k, m, x):
    return (x*k*5/7 + m - x*(x+1)/2)

def half(k, m, a, b, eps):
    c = (a + b) / 2
    if f(k,m,c) == 0:
        return c
    while (b - a) >= eps:
        if f(k,m,a) * f(k,m,c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
    return c


def main():
    with open("input.txt") as inFile:
        for line in inFile:
            k, m, d = [int(i) for i in line.split()]
    exactDate = 0
    if (d == 7 or d == 6) and m == 0:
        exactDate = 0
    elif d == 6 and (m == 1 or m == 2):
        exactDate = 1
    else:
        approximateDate = int(half(k, m, 0, k*2 + m*2, .0001))
        if approximateDate < 15:
            approximateDate = 15 
        for i in range(approximateDate - 14, approximateDate + 14):
            if books(i, k, d, m) < readForDays(i):
                exactDate = i - 1   
                break  
                
    of = open('output.txt', 'w')
    of.write("%d" % exactDate)
    of.close()

if __name__ == '__main__':
    main()