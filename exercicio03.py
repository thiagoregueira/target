# Sequência a)
a = [1, 3, 5, 7]
proximo_a = a[-1] + 2 # somar 2 ao anterior gera o próximo
print(proximo_a)

# Resposta: 9

# Sequência b)
b = [2, 4, 8, 16, 32, 64]
proximo_b = b[-1] * 2 # multiplicar o anterior por 2 gera o próximo
print(proximo_b)

# Resposta: 128

# Sequência c)
c = [0, 1, 4, 9, 16, 25, 36]
proximo_c = (len(c))**2 # numero de elementos ao quadrado
print(proximo_c)

# Resposta: 49

# Sequência d)
d = [4, 16, 36, 64]
proximo_d = 10 * 10 # todos são quadrados perfeitos dos números pares de 1 a 10
print(proximo_d)

# Resposta: 100

# Sequência e)
e = [1, 1, 2, 3, 5, 8]
proximo_e = abs(e[-1] + e[-2]) # fibonacci
print(proximo_e)

# Resposta: 13

# Sequência f)
f = [2, 10, 12, 16, 17, 18, 19]
proximo_f = 200 # todos iniciam com a letra "d"
print(proximo_f)

# Resposta: 200