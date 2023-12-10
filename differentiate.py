def differentiate(equation, point):
    total = 0 #the value to return is initialized
    equation = '>' + equation #creates a character at the start of the equation so the pointer isn't looking at nothing
    pointer = len(equation) - 1 #the creation of the end pointer to begin looking through the equation
    while pointer > 0: #a while loop will look through the equation to make necessary changes
        if equation[pointer] == '-':
            equation = equation[:pointer] + '+' + equation[pointer:] #we will split along + so we need to add one to the -
        if equation[pointer] == 'x' and equation[pointer - 1] not in '0123456789':
            equation = equation[:pointer] + '1' + equation[pointer:] #adding a coefficient of 1 to x's
        pointer -= 1

    equation = equation[1:] #removing the > start character
    lst = equation.split('+') #creating a list of each term
    lst2 = [] #initializing a list for the split terms
    for i in lst: #a for loop splits each term into its coefficient and exponents, conveniently also dropping constants
        if 'x^' in i:
            lst2.append(i.split('x^'))
        elif 'x' in i:
            lst2.append(i.split('x'))

    for i in lst2: #a for loop runs through each split term and analyzes the derivative of the term at the indicated point
        if i[1] == '':
            total += int(i[0])
        else:
            total += int(i[0]) * int(i[1]) * point**(int(i[1]) - 1)

    return total
