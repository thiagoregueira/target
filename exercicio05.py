# String a ser invertida
string = input("Digite uma palavra: ")

# Inicializa a string invertida
string_invertida = ""

# Percorre a string de trás para frente
for i in range(len(string)-1, -1, -1):
    # Adiciona cada caractere na string invertida
    string_invertida += string[i]

# Imprime a string invertida
print(string_invertida)