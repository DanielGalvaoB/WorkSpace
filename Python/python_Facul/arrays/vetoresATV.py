#❑Exercício 07: Desenvolver um programa que leia dez elementos numéricos de um vetor A.
#Construir um vetor B do mesmo tipo, observando a seguinte lei de formação: se o valor do
#índice do vetor A for par, o valor deve ser multiplicado por 5; sendo ímpar, deve ser
#somado com 5. Ao final, mostrar o conteúdo dos vetores A e B

"""
FORMA 01
a = [1,2,3,4,5,6,7,8,9,10]
b =[]
for i, e in enumerate (a):
    if i %2 == 0:
        b.append(e*5)
    else:
        b.append(e+5)
print(f'{a}\n{b}')
"""

"""
FORMA 02
a = [1,2,3,4,5,6,7,8,9,10]
b =[0] * len(a)
for i, e in enumerate(a):
    if i %2 == 0:
        b[i] = 5 * e
    else:
        b[i] = 5 + e
print(f'{a}\n{b}')"""
"""
FORMA 03
a = [1,2,3,4,5,6,7,8,9,10]
b =[0] * len(a)
contador = 0
while contador < len(a):
    if contador %2 ==0:
        b[contador] = 5 * a[contador]
    else:
        b[contador] = 5 + a[contador]
    contador += 1

print(a)
print(b)
"""
#❑Exercício 08: Desenvolver um programa que leia cinco elementos numéricos inteiros de um
#vetor A. No final, apresentar o total da soma de todos os elementos do vetor A que sejam
#ímpares.
"""a = [1, 2, 3, 4, 5, 6, 7]
b = 0
for i in a:
    if i %2 != 0:
        b += i
print(f'a soma de todos os elementos de A ={a} é igual a {b}')"""

#❑Exercício 09: Elaborar um programa que efetue a leitura de dez nomes de pessoas e
# armazene em um vetor, apresente-os sem seguida.
"""
nomes = []
x = 0
while x < 10:
    n = input("diga seu nome:\n")
    nomes.append(n)
    x += 1
print(nomes)
"""
#❑Exercício 10: Elaborar um programa que leia oito elementos inteiros em um vetor A.
# Construir um vetor B de mesma dimensão com os elementos do vetor A multiplicados por
# 3. O elemento B[1] deve ser implicado pelo elemento A[1]*3, o elemento B[2] implicado
# pelo elemento A[2]*3 e assim por diante, até 8. Apresentar o vetor B.
"""
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = a.copy()
for i, e in enumerate (b):
    b[i] = b[i] * 3
print(a)
print(b)
"""
#❑Exercício 11: Escrever um programa que leia dois vetores (denominados A e B) com 20
# elementos reais. Construir um vetor C, sendo cada elemento do vetor C a subtração de um
# elemento correspondente do vetor A com um elemento correspondente do vetor B, ou
# seja, a operação de processamento deve estar baseada na operação C[i] = A[i] - B[i]. Ao
# final, apresentar os elementos do vetor C.
"""
a = list(range(20))
b = a.copy()

c = []
for i in range (20):
    c.append(a[i] - b[i])
print(a)
print(b)
print(c)
"""

#Elaborar um programa que leia 15 elementos inteiros de um vetor A.
# Construir um vetor B de mesmo tipo, observando a seguinte lei de formação: "todo
# elemento do vetor B deve ser o quadrado do elemento do vetor A correspondente".
# Apresentar os elementos dos vetores A e B.
"""
a = list(range(15))
b = []
for i, e in enumerate (a):
    b.append(a[i]**2)
print(a)
print(b)
"""

#❑Exercício 13: Elaborar um programa que leia um vetor A com 15 elementos inteiros.
# Construir um vetor B de mesmo tipo, e cada elemento do vetor B deve ser o resultado do
# fatorial correspondente de cada elemento do vetor A. Apresentar os vetores A e B.
"""
import math
a=list(range(15))
b = []

for i in a:
    b.append(math.factorial(a[i]))
print(a)
print(b)
"""

#❑Exercício 14: Construir um programa que leia dois vetores A e B com 15 elementos inteiros
# cada. Construir um vetor C, sendo este o resultado da junção dos vetores A e B. Desta
# forma, o vetor C deve ter o dobro de elementos em relação aos vetores A e B, ou seja, o
# vetor C deve possuir 30 elementos. Apresentar o vetor C.
"""
a = [10]*15
b = [20]*15
c = a + b

print(a)
print(b)
print(c)
"""
#❑Exercício 15: Elaborar um programa que leia 10 elementos do tipo real em um vetor A e
# construir um vetor B de mesma dimensão com os mesmos elementos armazenados no
# vetor A, porém de forma invertida. Ou seja, o primeiro elemento do vetor A passa a ser o
# último do vetor B, o segundo elemento de A passa a ser o penúltimo de B, e assim por
# diante. Apresentar os elementos dos vetores A e B.
"""
a = list(range(10))
b = a.copy()
b.reverse()

print(a)
print(b)
"""

#❑Exercício 16: Escrever um programa que leia três vetores (A, B e C) com cinco elementos
# cada que sejam do tipo real. Construir um vetor D, sendo este o resultado da junção dos
# três vetores (A, B e C). Desta forma, o vetor D deve ter o triplo de elementos dos vetores A,
# B e C, ou seja, 15 elementos. Apresentar os elementos do vetor D.

"""
a = [10] * 5
b = [20] * 5
c = [30] * 5
c.extend(a + b)
c.sort()

print(f"A = {a}\nB = {b}\nC = {c}")
"""

#❑Exercício 17: Elaborar um programa que leia um vetor A com 10 elementos inteiros.
# Construir um vetor B do mesmo tipo e dimensão do vetor A, sendo cada elemento do vetor
# B o somatório de 1 até o valor do elemento correspondente armazenado no vetor A. Se o
# valor do elemento do vetor A[1] for 5, o elemento correspondente do vetor B[1] deve ser
# 15, pois o somatório do elemento do vetor A é 1+2+3+4+5. Apresentar os elementos do
# vetor B.
"""
a = list(range(10))
b = []
for i in a:
    s = 0
    for x in range(1, i + 1):
        s += x
    b.append(s)
print(a)
print(b)"""

#❑Exercício 18: Elaborar um programa que leia um vetor A com dez elementos inteiros
# positivos. Construir um vetor B do mesmo tipo e dimensão, em que cada elemento do
# vetor B deve ser o valor negativo do elemento correspondente do vetor A. Desta forma, se
# em A[1] estiver armazenado o elemento 8, deve estar em B[1] o valor –8 e assim por
# diante. Apresentar os valores dos vetores A e B.
"""
a = list(range(10))
b = [-x for x in a]
print(a)
print(b)
"""
#❑Exercício 19: Elaborar um programa que leia um vetor A com dez elementos inteiros.
# Construir um vetor B de mesmo tipo, em que cada elemento deve ser a metade de cada
# um dos elementos existentes no vetor B. Apresentar os elementos dos vetores A e B.
"""
a = [10] * 10
b = []
for i, e in enumerate(a):
    b.append(e/2)
print(a)
print(b)
"""
#❑Exercício 20: Construir um programa que calcule a tabuada de um valor qualquer de 1 até
# 10 e armazene os resultados em um vetor A. Apresentar os elementos do vetor A.
# Lendo o valor para a tabuada
"""
v = int(input("Diga um valor: "))
A = []

i = 1
while i<10:
    A.append(v * i)
    i += 1
print(A)
"""
#❑Exercício 21: Elaborar um programa que leia 10 elementos (valores reais) para
# temperaturas e graus Celsius e armazene esses valores em um vetor A. O programa ao final
# deve apresentar a menor, a maior e a média das temperaturas lidas.
"""
a = []

for i in range(10):
    t = int(input("informe a temperatura: "))
    a.append(t)

print(f"menor temperatura: {min(a)}\nMaior Temperatura: {max(a)}\nMedia de temperaturas: {sum(a)/len(a)}")

"""
#❑Exercício 22: Escrever um programa que leia cinco elementos (valores reais) para
# temperaturas em graus Celsius e armazene esses valores em um vetor A. Construir um
# vetor B de mesmo tipo e dimensão, em que cada elemento do vetor B deve ser a conversão
# da temperatura em Fahrenheit do elemento correspondente do vetor A. Apresentar os
# elementos dos vetores A e B.
"""
a = []
b = []
for i in range(10):
    t = int(input("informe a temperatura: "))
    a.append(t)
    b.append(int(a[i]*1.8+32))
print(f"temperaturas em graus Celcios: {a}")
print(f"temperaturas em graus Fahrenheit {b}")

"""

#❑Exercício 23: Elaborar um programa que leia 10 elementos inteiros para um vetor A.
# Construir um vetor B de mesmo tipo e dimensão, observando a seguinte lei de formação:
# "todo elemento do vetor A que for ímpar deve ser multiplicado por 2; caso contrário, o
#  elemento do vetor A deve permanecer constante". Apresentar os elementos do vetor B.
"""
A = []

for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    A.append(elemento)
B = []
for x in A:
    if x % 2 != 0:
        B.append(x * 2)
    else:
        B.append(x)
print(F"{A}\n{B}")
"""
#❑Exercício 24: Elaborar um programa que leia 10 elementos reais para um vetor A. Construir
# um vetor B de mesmo tipo e dimensão, observando a seguinte lei de formação: "todo
# elemento do vetor A que possuir índice par deve ter seu elemento dividido por 2; caso
# contrário, o elemento do vetor A deve ser multiplicado por 1.5". Apresentar os elementos
# do vetor B.
"""
A = []
for i in range(10):
    num = float(input(f"Digite o elemento {i+1} do vetor A: "))
    A.append(num)

B = []
for i in range(10):
    if i % 2 == 0:
        B.append(A[i] / 2)
    else:
        B.append(A[i] * 1.5)

print("Elementos do vetor B:")
print(B)

"""
"""
#❑Exercício 25: Elaborar um programa que leia 6 elementos (valores inteiros) para os vetores
A e B. Construir os vetores C e D de mesmo tipo e dimensão. O vetor C deve ser formado
pelos elementos de índice ímpar dos vetores A e B e o vetor D deve ser formado pelos
elementos de índice par dos vetores A e B. Apresentar os elementos dos vetores C e D.

A = []
B = []

for i in range(6):
    A.append(int(input(f"Digite o elemento {i+1} do vetor A: ")))
    B.append(int(input(f"Digite o elemento {i+1} do vetor B: ")))

C = []
D = []

for i in range(6):
    if i % 2 == 1:
        C.append(A[i])
        C.append(B[i])
    else:
        D.append(A[i])
        D.append(B[i])

print("Elementos do vetor D:", D)
print("Elementos do vetor C:", C)
"""
"""❑Exercício 26: Elaborar um programa que leia dois vetores A e B com seis elementos. O
vetor A deve aceitar apenas a entrada de valores pares, enquanto o vetor B deve aceitar
apenas a entrada de valores ímpares. A entrada dos vetores deve ser validada pelo
programa e não pelo usuário. Construir um vetor C que seja o resultado da junção dos
vetores A e B, de modo que o vetor C tenha 12 elementos. Apresentar os elementos do
vetor C.

A = []
B = []

while len(A) < 6:
    num = int(input("Digite um valor par para o vetor A: "))
    if num % 2 == 0:
        A.append(num)
    else:
        print("Valor inválido! O número deve ser par.")

while len(B) < 6:
    num = int(input("Digite um valor ímpar para o vetor B: "))
    if num % 2 != 0:
        B.append(num)
    else:
        print("Valor inválido! O número deve ser ímpar.")

C = A + B

print("Elementos do vetor C:", C)
"""
"""
❑Exercício 27: Construir um programa que leia um vetor A com dez elementos inteiros. Ao
final do programa, apresentar a quantidade de valores pares e ímpares existentes no
referido vetor.

A = []

for i in range(10):
    num = int(input(f"Digite o elemento {i+1} do vetor A: "))
    A.append(num)

pares = sum(1 for x in A if x % 2 == 0)
impares = sum(1 for x in A if x % 2 != 0)

print("Quantidade de valores pares:", pares)
print("Quantidade de valores ímpares:", impares)
"""

"""
❑Exercício 28: Elaborar um programa que leia dois vetores A e B com dez elementos inteiros
cada. Construir um vetor C de mesmo tipo e dimensão que seja formado pelo quadrado da
soma dos elementos correspondentes dos vetores A e B. Apresentar os elementos do vetor
C.

A = []
B = []

for i in range(10):
    A.append(int(input(f"Digite o elemento {i+1} do vetor A: ")))
    B.append(int(input(f"Digite o elemento {i+1} do vetor B: ")))

C = [(A[i] + B[i]) ** 2 for i in range(10)]

print("Elementos do vetor C:", C)
"""
"""
❑Exercício 29: Elaborar um programa que leia um vetor com 10 elementos numéricos
inteiros. Apresentar o total de elementos pares e ímpares existentes no vetor e também o
percentual do valor total de números pares e ímpares em relação à quantidade total de
elementos armazenados no vetor.

A = []

for i in range(10):
    num = int(input(f"Digite o elemento {i+1} do vetor: "))
    A.append(num)

pares = sum(1 for x in A if x % 2 == 0)
impares = sum(1 for x in A if x % 2 != 0)

total_elementos = len(A)
percentual_pares = (pares / total_elementos) * 100
percentual_impares = (impares / total_elementos) * 100

print("Total de elementos pares:", pares)
print("Total de elementos ímpares:", impares)
print(f"Percentual de números pares: {percentual_pares:.2f}%")
print(f"Percentual de números ímpares: {percentual_impares:.2f}%")
"""





