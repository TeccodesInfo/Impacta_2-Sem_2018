'''
def calcular_estatisticas(numeros):
    #Seu Código vai Aqui!
     maior,menor,media,soma = 0,0,0,0
     menor = numeros[0]
     maior = numeros[0]
     menor = numeros[0]
     soma = 0
     cont = 0
     for n in numeros:
         if n < menor:
             menor = n
         if n > maior:
             maior = n
         soma = soma + n
         cont = cont + 1
     media = soma/cont
     return maior, menor, media,soma
'''
'''
def calcular_estatisticas2(numeros):
    menor = min(numeros)
    maior = max(numeros)
    soma = sum(numeros)
    media = soma / len(numeros)

    return maior,menor,media,soma

assert(calcular_estatisticas2([1,2,3]) == (3,1,2.0,6))
assert(calcular_estatisticas2([2,2,2]) == (2,2,2.0,6))
assert(calcular_estatisticas2([5,6,1]) == (6,1,4.0,12))
'''
'''
bimestre_final = 6

notas = {
    "aluno1": [],
    "aluno2": [],
}

notas = {}
alunos = ["Patricia", "Sabrina"]
bimestres = ["{} Bim".format(numero) for numero in range(1, 5)]

# esse é o for sem a list comprehenssion ai de cima
#
# bimestres = []
# for numero in range(1, 7):
#    bimestres.append("{} Bim".format(numero))
#

pesos = {
    "1 Bim": 10.0,
    "2 Bim": 10.0,
    "3 Bim": 10.0,
    "4 Bim": 10.0,
}

for aluno in alunos:
    print("Aluno: ", aluno)
    notas[aluno] = {}
    for bimestre in bimestres:
        nota = input("Digite a nota do {}: ".format(bimestre))
        nota = float(nota)
        notas[aluno][bimestre] = nota

# (5*2 + 4*3 + 3*3 + 2*4 + 1*5) /
# (2 + 3 + 3 + 4 + 5 + 5) = 7.40
numerador = {}
denominador = {}
for aluno in alunos:
    numerador[aluno] = 0
    denominador[aluno] = 0
    for bimestre, nota in notas[aluno].items():
        peso = pesos[bimestre]
        numerador[aluno] += nota * peso
        denominador[aluno] += peso

resultado_final = {}
for aluno in alunos:
    resultado_final[aluno] = numerador[aluno] / denominador[aluno]

# Nota maior que 9 teve menção A
# Nota maior que 7 e menor ou igual a 9 teve menção B
# Nota maior que 5 e menor ou igual a 7 teve menção C
# Nota menor que 5 teve menção D

for nome, nota in resultado_final.items():
    print("Nota final {}: {}".format(nome, nota))

    if nota > 5:
        print("Nota A")
    elif 10 >= nota > 7:
        print("Nota B")
    elif 10 >= nota > 5:
        print("Nota C")
    else:
        print("Nota D")
'''
'''
semana = [ 'Segunda','Terça','Quarta','Quinta','Sexta']
tupla_semana = tuple(semana)
print(tupla_semana)
'''
'''
semana =('Segunda','Terça','Quarta','Quinta','Sexta')
lista_semana = list(semana)
print(lista_semana)
print(type(lista_semana))
'''
'''
class Veiculo:
	numeroDeRodas = 0

triciclo = Veiculo()
triciclo = Veiculo()
print(triciclo.numeroDeRodas)
triciclo.numeroDeRodas = 3
print(triciclo.numeroDeRodas)
'''
'''
class Televisao:
	def __init__(self):
		self.ligada = True
		self.canal = 2

tv = Televisao()
print("Canal: %d" % (tv.canal))
print("Ligada: %s" % (tv.ligada))
'''
'''
class Televisao:
	def __init__(self):
		self.ligada = True
		self.canal = 2
	
	def aumenta_canal(self):
		print("Aumentar canal")

	def diminui_canal(self):
		print("Diminuir canal")
tv = Televisao()
tv.aumenta_canal()
tv.diminui_canal()
'''
'''
class Televisao:
	def __init__(self, min, max):
		self.ligada = True
		self.canal = 2
		self.cmin = min
		self.cmax = max
tv_sala = Televisao(2, 50)
'''
'''
class Televisao:
	def __init__(self, min = 2, max = 15):
		self.ligada = True
		self.canal = 2
		self.cmin = min
		self.cmax = max


tv_quarto = Televisao()
tv_sala = Televisao(2, 50)
'''
'''
class Televisao:
	def __init__(self, min = 2, max = 20):
		self.ligada = True
		self.canal = 2
		self.__cmin = min
		self.__cmax = max
'''
'''
class Televisao:
    def __init__(self,min = 2,max = 20):
        self.ligada = True
        self.canal = 2
        self.___cmin = min
        self.___cmax = max
                
    def aumenta_canal(self):
        print("Aumentar canal")
        self.canal = self.canal + 1
        if(self.canal > self.___cmax):
            self.canal = self.___cmin

    def diminui_canal(self):
         print("Diminuir canal")
         self.canal = self.canal - 1
         if(self.canal < self.___cmin):
             self.canal = self.___cmax

		
tv = Televisao(2,5)
for i in range(10):
    tv.aumenta_canal()
    print(tv.canal)
'''

