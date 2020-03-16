import random, sys

#def Oct():
#    RN = random.randint(0, 4)
#
#    if RN == 0:
#        print("''")
#    elif RN == 1:
#        print("'")
#    elif RN == 2:
#        print("g")
#    elif RN == 3:
#        print(",")
#    elif RN == 4:
#        print(",,")

def Solo():
    # A establece la Nota o Silencio (0 - 11 = Nota | 12 - 15 = Silencio)(RN1)
    # B establece la Octava en la que va a sonar la Nota(RN2)
    # C establece la duración de la nota o silencio (RN3)
    A = None
    B = None
    C = None
    RN1 = random.randint(0, 15)
    RN2 = random.randint(1, 3)
    RN3 = random.randint(0, 6)


    #Esta sección estblece Si va a haber silencio o nota, y si hay, cual va a ser
    note = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b", "r", "r", "r", "r"]
    A = note[RN1]


    #Esta sección establece la octava
    octava = ["''","'" , "", ",", ",,"]
    B = octava[RN2]

    # Esta seccion establece la duración
    duración = ["1 ", "2 ", "4 ", "8 ", "16 ", "32 ", "64 "]
    C = duración[RN3]


    # Duraciones
    cont=[4.0, 2.0, 1.0, 0.5, 0.25, 0.125, 0.0625]
    vuelta=cont[RN3]

    #Comando que imprime el resultado (a cambiar en futuras versiones)


    from pathlib import Path
    if RN1 <= 11:
        textFile = open('Solo.txt', 'a')
        textFile.write(A + B + C)
        textFile.close()
        print(A + B + C)
        print(vuelta)
    else:
        textFile = open('Solo.txt', 'a')
        textFile.write(A + C)
        textFile.close()
        print(A + C)
        print(vuelta)

h=0 #acá estoy buscando hacer un contador para aplicar el comando '\baar ""', que en el lilipond sirve para hacer un salto de compas
i=0
while i<3:
    Solo()

    i+=1

    if h != 4:
        h += 1
    elif h == 4:
        h = h -4
    print (h)
#\bar #con bar se separa el compas