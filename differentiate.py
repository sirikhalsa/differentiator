def differentiate(equation, point):
    total = 0
    equation = '>' + equation
    pointer = len(equation) - 1
    while pointer > 0:
        if equation[pointer] == '-':
            equation = equation[:pointer] + '+' + equation[pointer:]
        if equation[pointer] == 'x' and equation[pointer - 1] not in '0123456789':
            equation = equation[:pointer] + '1' + equation[pointer:]
        pointer -= 1
    equation = equation[1:]
    lst = equation.split('+')
    lst2 = []
    for i in lst:
        if 'x^' in i:
            lst2.append(i.split('x^'))
        elif 'x' in i:
            lst2.append(i.split('x'))

    for i in lst2:
        if i[1] == '':
            total += int(i[0])
        else:
            total += int(i[0]) * int(i[1]) * point**(int(i[1]) - 1)

    return total
