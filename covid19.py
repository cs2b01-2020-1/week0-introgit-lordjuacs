#FUNCIONES
def comparar(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")
    text1 = str(f1.read())
    text2 = str(f2.read())
    f1.close()
    f2.close()

    menor = min(len(text1), len(text2))
    simi = 0
    for i in range(menor):
        if text1[i] == text2[i]:
            simi+=1

    proporcion = (simi/len(text1))*100
    return round(proporcion,2)

def imprimir(lista):
    print("COMPARACION")
    for x in range(len(lista)):
        print(lista[x] + "\t= file" + str(x+1))
    print()
    print("\t", end="")

    for y in range(len(lista)):
        print("file" + str(y+1), end="\t")
    print()

    for i in range(len(lista)):
        print("file" + str(i + 1), end="\t")
        for j in range(len(lista)):
            porcentaje = comparar(lista[i], lista[j])
            if i != j:
                print(porcentaje, end="\t")
            else: print("=====", end="\t")
        print()




#MAIN
archivos = ["genomas/AY274119.txt", "genomas/AY278488.2.txt",
            "genomas/MN908947.txt", "genomas/MN988668.txt",
            "genomas/MN988669.txt"]

imprimir(archivos)


