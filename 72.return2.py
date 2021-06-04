numList = []


def PythonList(start, end):
    for x in range(start, end):
        if x % 2 == 0:
            numList.append(x)
    return numList


print PythonList(4, 30)
