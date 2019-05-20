Str = input()
for i in range(len(Str)):
    if i == '+':
        M = eval(Str[:Str.find('+')])
        N = eval(Str[Str.find('+') + 1:])
        print("{:.2f}".format(M + N))
    if i == '-':
        M = eval(Str[:Str.find('-')])
        N = eval(Str[Str.find('-') + 1:])
        print("{:.2f}".format(M - N))
    if i == '*':
        M = eval(Str[:Str.find('*')])
        N = eval(Str[Str.find('*') + 1:])
        print("{:.2f}".format(M * N))
    if i == '/':
        M = eval(Str[:Str.find('/')])
        N = eval(Str[Str.find('/') + 1:])
        print("{:.2f}".format(M / N))