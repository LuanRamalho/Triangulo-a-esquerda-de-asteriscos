rows = 9
# Primeiro lado direito para baixo
for i in range(0, rows - 1):
    # Imprimir espaços à esquerda
    for j in range(i, rows - 1):
        print(" ", end=" ")
    # Imprimir asteriscos à direita
    for j in range(0, i + 1):
        print("*", end=" ")
    print("\r")

# Segundo lado direito para cima
for i in range(rows, 0, -1):
    # Imprimir espaços à esquerda
    for j in range(i, rows):
        print(" ", end=" ")
    # Imprimir asteriscos à direita
    for j in range(0, i):
        print("*", end=" ")
    print("\r")

input()
