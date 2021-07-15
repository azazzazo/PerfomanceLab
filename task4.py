a, b = input().split()

if not '*' in b:
    if a == b:
        print('OK')
    else:
        print('KO')
else:
    for i in range(len(a)):
        if b[i] == '*':
            print('OK')
            quit()
        elif a[i] != b[i]:
            print('KO')
            quit()
    print('KO')