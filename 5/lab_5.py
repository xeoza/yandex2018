from math import sqrt

def books(days, k, begin, m):
    # количество книг, которые мог прочитать Коля за 'days' дней
    result = 5 * int(days / 7)

    if days % 7 == 0:
        return k * result + m

    end = begin + days % 7
    result += end - begin
    if begin <= 6 and end >= 8:
        result -= 2
    elif begin == 7 or end == 7:
        result -= 1

    if result > 0:
        return k * result + m

    return m

def f(k, m, x):
    return (x*k*5/7 + m - int(x*(x+1)/2))

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

def read_books(days):
    # количество книг, которое Коля должен был прочитать за 'days' дней
    return int((days + 1) * days / 2)




if __name__ == '__main__':
    # while True:
    #     k, m, d = map(int, input().split())
    #
    #     if d == 7 and m == 0 or d == 6 and m < 2:
    #         print(0)
    #     else:
    #         b = (1 - 10 * k / 7) / 2  # промежуточное значение
    #         approximate_day = int(sqrt(b ** 2 + 2 * m) - b)  # примерное количество дней
    #         if approximate_day < 32:
    #             approximate_day = 32
    #
    #         for i in range(approximate_day - 31, approximate_day + 31):
    #             if books(i, k, d, m) < read_books(i):
    #                 print(i - 1)
    #                 break
    #
    #     book = m
    #     day = d
    #     result = 0
    #     books_in_day = 1
    #     while True:
    #         if day <= 5:
    #             book += k
    #         book -= books_in_day
    #         day += 1
    #         if day == 8:
    #             day = 1
    #         if book < 0:
    #             break
    #         result += 1
    #         books_in_day += 1
    #
    #     print(result, end='\n\n')

    first_result = 0
    count = 0
    for k in range(1, 100):
        for m in range(100):
            for d in range(1, 8):
                
                if (d == 7 or d == 6) and m == 0:
                    first_result = 0
                elif d == 6 and (m == 1 or m == 2):
                    first_result = 1
                else:
                    koren = int(half(k, m, 0, k*2 + m*2, .0001))
                    if koren < 15:
                        koren = 15 
                    for i in range(koren - 14, koren + 14):
                        if books(i, k, d, m) < read_books(i):
                            first_result = i - 1   
                            break



                #first_result = round(koren)
                '''
                if (d == 7 or d == 6) and m == 0:
                    first_result = 0
                elif d == 6 and (m == 1 or m == 2):
                    first_result = 1
                else:
                    b = (1 - 10 * k / 7) / 2  # промежуточное значение
                    approximate_day = int(sqrt(b ** 2 + 2 * m) - b)  # примерное количество дней
                    if approximate_day < 32:
                        approximate_day = 32

                    for i in range(approximate_day - 31, approximate_day + 31):
                        if books(i, k, d, m) < read_books(i):
                            first_result = i - 1
                            break'''
                book = m
                day = d
                result = 0
                books_in_day = 1
                while True:
                    if day <= 5:
                        book += k
                    book -= books_in_day
                    day += 1
                    if day == 8:
                        day = 1
                    if book < 0:
                        break
                    result += 1
                    books_in_day += 1
                if result != first_result:
                    count += 1
                    print(k,m,d,'|',koren,'|',result, first_result,'|', koren)
                    #print(k, m, d)
    print(count,'/',100*100*7)