def main():
    with open("input.txt") as inf:
        for line in inf:
            k, m, d = [int(i) for i in line.split()]
    answer = 0
    booksInDay = 1
    while True:
        if d <= 5:
            m += k
        m -= booksInDay
        d += 1
        if d == 8:
            d = 1
        if m < 0:
            break
        answer += 1
        booksInDay += 1

    of = open('output.txt', 'w')
    of.write("%d" % answer)
    of.close()
if __name__ == '__main__':
    main()