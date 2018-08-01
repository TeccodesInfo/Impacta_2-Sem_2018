'''
x = 0

n =int(input("Digite um Número: "))

result = 1

lista = range(1,n+1)
for x in lista:
    result = x * result
'''
'''
numeros = [10,20,30,40]
x = [ i for i in numeros if numeros.count(i) <2]
max_value = max(x)
min_value = min(x)
print(max_value)
print(min_value)
'''
'''
numeros = [5,2,1,6,7,8,9,20,24]
maior = numeros[0]
menor = numeros[0]
contador = 0
total = 0
for n in numeros:
    if n> maior:
        maior = n
    if n<menor:
        menor = n
    total = total + n
    contador = contador + 1
media = total / contador
print("0 Maior Elemento: %d" %(maior))
print("0 Menor Elemento: %d" %(menor))
print("A Média: %d" %(media))
'''
