fila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    sistema = input("precione 'f' para adicionar alguem, 'a' para remover ou fechar: ") 
    if sistema == 'f':

     fila.append(len(fila) + 1) 

     print(fila)

    elif sistema == 'a': 

        del fila[0] 

        print(fila)

    elif sistema == 's': 

        print(fila)
        break