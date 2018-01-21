for i in range(int(input())):
    a, b = input().split()
    try:
        c = int(a)//int(b)
        print(c)
    except ZeroDivisionError:
        print('Error Code: ')
        continue
    except ValueError as e:
        print('Error Code: ' + e)
        continue

