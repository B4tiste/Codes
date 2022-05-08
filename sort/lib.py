import random

def createRandomTable(size, border):
    """
        Given a size and a a border array, return a size long table 
        filled with random numbers
    """
    return [random.randint(border[0], border[1]) for i in range(size)]

def bubbleSort(table):
    """
        Given a table, sort it with bubble sort
    """
    for i in range(len(table)):
        for j in range(len(table) - 1):
            if table[j] > table[j + 1]:
                table[j], table[j + 1] = table[j + 1], table[j]
    return table

def insertionSort(table):
    """
        Given a table, sort it with insertion sort
    """
    for i in range(1, len(table)):
        j = i
        while j > 0 and table[j] < table[j - 1]:
            table[j], table[j - 1] = table[j - 1], table[j]
            j -= 1
    return table
    