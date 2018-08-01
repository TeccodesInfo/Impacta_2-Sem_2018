'''
x = 0
n = int(input("Digite um Número: "))
result = 1
lista = range(1,n+1)
for x in lista:
    result = x * result
'''
'''
entrada = [1,2,5,6,9,4]
print(entrada [0::2])
'''
'''
dic_maluco = {x: x*x for x in range(100) if  x % 2 ==1}
print(dic_maluco)
'''
'''
def contar_palavras(texto):
#Escreva seu Código(Comentário:)
    lista_palavras = texto.splint()
    contadores_palavras = {}
    for palavra in lista_palavras:
        if palavra not in contadores_palavra:
            contadores_palavra[palavra] = 1
        else:
            contadores_palavra[palavra] += 1
    return contadores_palavra

palavra = str(input("Digite seu Texto:"))
contador = conta_palavras(palavra)
print(contador)
'''

