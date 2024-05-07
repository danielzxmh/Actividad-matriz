abc = [['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-'],['-','-','-','-','-','-']]


    
def fnt_agregar(dato, x, y):

    if dato == 'a' or "A" and (x == 0 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'b' or "B" and (x == 0 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'c' or "C" and (x == 0 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'd' or "C" and  (x == 0 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'e' or "E" and (x == 0 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'f' or "F" and (x == 0 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'g' or "G" and (x == 1 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'h' or "H" and (x == 1 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'i' or "I"and (x == 1 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'j' or "J"and (x == 1 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'k' or "K" and (x == 1 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'l' or "L"and (x == 1 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'm' and (x == 2 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'n' or "N"and (x == 2 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'ñ' or "Ñ"and (x == 2 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'o' or "O"and (x == 2 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'p' or "P" and (x == 2 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'q' or "Q"and (x == 2 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'r' or "R"and (x == 3 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 's' or "S"and (x == 3 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 't' or "T"and (x == 3 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'u' or "U"and (x == 3 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'v' or "V"and (x == 3 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'w' or "W"and (x == 3 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'x' or "X"and (x == 4 and y == 0):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'y' or "Y"and (x == 4 and y == 1):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'z' or "Z"and (x == 4 and y == 2):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'ch' or "CH"and (x == 4 and y == 3):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()  
    elif dato == 'll' or "LL"and (x == 4 and y == 4):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    elif dato == 'rr' or "RR"and (x == 4 and y == 5):
        if abc[x][y] == '-':
            abc[x][y] = dato.upper()
    else:
        input('\nEsta letra no esta en su posición adecuada <ENTER>')

def fnt_impresion_matriz():
    for i in range(len(abc)):
        for j in range(len(abc[i])):
            print(abc[i][j], end='  ')
        print()
        
sw = True
while sw == True:
    import os
    os.system('cls')
    fnt_impresion_matriz()
    fnt_agregar(input('Dato: '), int(input('Fila: ')), int(input('Columna: ')))