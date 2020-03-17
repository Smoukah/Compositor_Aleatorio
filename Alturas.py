#
# Bueno, está all desordenado, pero acá lo que hice es agregar duraciones que faltaban (los puntillos) y... bueno, logré poco más
# 'todo' me pone las letras de color verde... no tengo idea por qué
#   también cambié la extensión .txt por .ly, que es en la que se ejecuta Lilypond.
#   Además agregué texto para que Solo.ly se pueda ejecutar apenas sale con lilypond.
#   (el texto está´copiado, pegado y adaptado para que funcione, en otro momento puedo mejorar eso, pero me interesan más otras cosas en este momento)
#
#
import random, sys

textFile = open('Solo.ly', 'w')  # agregué esta linea para que cree el archivo Solo.ly cada vez que se ejecuta el programa


def Solo():
    # A establece la Nota o Silencio (0 - 11 = Nota | 12 - 15 = Silencio)(RN1)
    # B establece la Octava en la que va a sonar la Nota(RN2)
    # C establece la duración de la nota o silencio (RN3)
    A = None
    B = None
    C = None
    RN1 = random.randint(0, 15)
    RN2 = random.randint(1, 3)
    RN3 = random.randint(0, 20)

    # Esta sección estblece Si va a haber silencio o nota, y si hay, cual va a ser
    note = ["c", "cis", "d", "dis", "e", "f", "fis", "g", "gis", "a", "ais", "b", "r", "r", "r", "r"]
    A = note[RN1]

    # Esta sección establece la octava
    octava = ["''", "'", "", ",", ",,"]
    B = octava[RN2]

    # Esta seccion establece la duración
    duración = ["1 ", "1. ", "1.. ", "2 ", "2. ", "2.. ", "4 ", "4. ", "4.. ", "8 ", "8. ", "8.. ", "16 ", "16. ",
                "16.. ", "32 ", "32. ", "32.. ", "64 ", "64. ", "64.. "]
    C = duración[RN3]

    # Duraciones (hay 23 aquí con los valores correspondientes a '128' y '256' (garrapatea y semigarrapatea respectivamente) *Lilypond hacepta hasta la garrapatea,
    # duraciones más breves deven estar unidas a otras con barras)
    cont = [4.0, 6.0, 7.0, 2.0, 3.0, 3.5, 1.0, 1.5, 1.75, 0.5, 0.75, 0.885, 0.25, 0.375, 0.4375, 0.125, 0.1875, 0.21875,
            0.0625, 0.09375, 0.109375, 0.03125, 0.015625]
    vuelta = cont[RN3]

    # Comando que imprime el resultado (a cambiar en futuras versiones)

    from pathlib import Path
    if RN1 <= 11:
        textFile = open('Solo.ly', 'a')
        textFile.write(A + B + C)
        textFile.close()
        print(A + B + C)
        print(vuelta)
    else:
        textFile = open('Solo.ly', 'a')
        textFile.write(A + C)
        textFile.close()
        print(A + C)
        print(vuelta)

textFile = open('Solo.ly', 'a')
textFile.write('\\version "2.20.0"  % necessary for upgrading to future LilyPond versions.\n\header\n\t{\n\ttitle = "Prueba Solo"\n\tsubtitle = "La batalla comienza"\n\t\n\n\\score {\n\\layout{}\n\\midi{}\n\\new Staff {\n\\absolute\n\\clef C\n\\time 2/4\n\\cadenzaOn\n{\n')
textFile.close()
print('\\version "2.20.0"  % necessary for upgrading to future LilyPond versions.\n\header\n\t{\n\ttitle = "Prueba Solo"\n\tsubtitle = "La batalla comienza"\n\t\n\n\\score {\n\\layout{}\n\\midi{}\n\\new Staff {\n\\absolute\n\\clef C\n\\time 2/4\n\\cadenzaOn\n{\n')

#acá experimento como hacer la separación, no sabia como poner el caracter \, sn embargo ya leí como hacerlo... el problema ahora es el resto jaja
# 24
#e = 0
#while e < 4:
#    j = 0
#
#    if j < 5:
#        Solo()
#        e += 1
#        j += 1
#    elif j == 5:
#        [\,a]
#        textFile = open('Solo.txt', 'a')
#        textFile.write('\\bar ""')
#        textFile.close()
#        j = j - 5
#        e += 1

h = 0  # acá también estoy buscando hacer un contador para aplicar el comando '\bar ""', que en el lilipond sirve para hacer un salto de compas
i = 0
while i<9:
    Solo()
    i+=1

#    if h != 4:
#        h += 1
#    elif h == 4:
#        h = h -4
#    print (h)
# \bar #con bar se separa el compas


textFile = open('Solo.ly', 'a')
textFile.write('}\n}\n}')
textFile.close()
