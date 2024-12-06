breaks = [" ", "\n"]

#Separating Lines
def lines():
    file = open("input.txt", "r")

    for line in file:
        if line.startswith("\n"):
            f.write("\n")
        else:
            Space = True
            for x in line:
             if (Space):
                    f.write("")
                    break
            if (not (x == "\n" or x == " ")):
                    rating(line)
                    Space = False

#Calculating and controlling
integers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
matops = ["!","%","/","//" ,"**","*","+","-","<",">","!=","=="]
result = ["!", "="]
def ops(variables):
    #Calculating multiplication
    if ("*" in variables):
        i = variables.index("*")
        result = variables[i - 1] * variables[i + 1]
        variables.pop(i + 1)
        variables.pop(i)
        variables[i - 1] = result
    #Calculating division
    elif ("/" in variables):
        i = variables.index("/")
        if (variables[i + 1] == 0):
            f.write("ERROR\n")
            return -1
        result = variables[i - 1] / variables[i + 1]
        variables.pop(i + 1)
        variables.pop(i)
        variables[i - 1] = result
    #Calculating power
    elif ("**" in variables):
        i = variables.index("**")
        result = variables[i - 1] ** variables[i + 1]
        variables.pop(i + 1)
        variables.pop(i)
        variables[i - 1] = result
    #Calculating division with integers.
    elif ("//" in variables):
        i = variables.index("//")
        result = variables[i - 1] // variables[i + 1]
        if (variables[i + 1] == 0):
            f.write("ERROR\n")
            return -1
        variables.pop(i + 1)
        variables.pop(i)
        variables[i - 1] = result
    elif ("%" in variables):
        i = variables.index("%")
        result = variables[i - 1] % variables[i + 1]
        variables.pop(i + 1)
        variables.pop(i)
        variables[i - 1] = result
    #Calculating subs
    elif ("-" in variables):
        i = variables.index("-")
        result = variables[i - 1] - variables[i + 1]
        variables.pop(i + 1)
        variables.pop(i)
        variables[i - 1] = result
    #Calculating sum
    elif ("+" in variables):
        i = variables.index("+")
        result = variables[i - 1] + variables[i + 1]
        variables.pop(i + 1)
        variables.pop(i)
        variables[i - 1] = result
    elif ("<" in variables):
        i = variables.index("<")
        result = variables[i - 1] < variables[i + 1]
        variables.pop(i + 1)
        variables.pop(i)
        variables[i - 1] = result
    elif (">" in variables):
        i = variables.index(">")
        result = variables[i - 1] > variables[i + 1]
        variables.pop(i + 1)
        variables.pop(i)
        variables[i - 1] = result
    elif ("!=" in variables):
        i = variables.index("!=")
        result = variables[i - 1] != variables[i + 1]
        variables.pop(i + 1)
        variables.pop(i)
        variables[i - 1] = result
    elif ("==" in variables):
        i = variables.index("==")
        result = variables[i - 1] == variables[i + 1]
        variables.pop(i + 1)
        variables.pop(i)
        variables[i - 1] = result

    if (len(variables) > 1):
        ops(variables)
    else:
        f.write(str(variables[0]) + "\n")
def rating(expression):
    elements = []
    temp = ""
    integersFlag = False
    operatorFlag = False
    errorFlag = False
    for x in expression:

        if x in integers:
            if (operatorFlag):
                elements.append(temp)
                temp = ""
                operatorFlag = False
            temp = temp + x
            numberFlag = True
        elif x in matops or x in result:
            if (numberFlag):
                elements.append(int(temp))
                temp = ""
                numberFlag = False
            temp = temp + x
            operatorFlag = True
        elif x in breaks:
            if (numberFlag):
                elements.append(int(temp))
                temp = ""
                numberFlag = False
            if (operatorFlag):
                elements.append(temp)
                temp = ""
                operatorFlag = False
        else:
            errorFlag = True
            break

    if (errorFlag):
        f.write("ERROR\n")
    else:
        for x in elements:
            if (not (x in matops or isinstance(x, int))):
                f.write("ERROR\n")
                return -1
        try:
            ops(elements)
        except:
            f.write("ERROR\n")

f = open("output.txt",'a')
lines()