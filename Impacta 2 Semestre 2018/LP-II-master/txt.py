class Disciplina:
    pass
 
class Professor:
    def __init__(self, nome = '', email = '', ra = '', celular = ''):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__cargaHoraria = 0
        self.__disciplinas = []
 
    def get_nome(self):
        return self.__nome
 
    def set_nome(self, nome):
        self.nome = nome
 
    def get_email(self):
        return self.__email
 
    def set_email(self, email):
        self.__email = email
 
    def get_ra(self):
        return self.__ra
 
    def set_ra(self, ra):
        self.__ra = ra
 
    def get_celular(self):
        return self.__celular
 
    def set_celular(self, celular):
        self.__celular = celular
 
    def get_cargaHoraria(self):
        return self.__cargaHoraria
    
    def retorna_sobrenome(self):
        return self.__nome.split()[-1]
 
    def adicionar_disciplina(self, disciplina):
        if (self.__ra == disciplina.get_professor().get_ra()):
            self.__disciplinas.append(disciplina)
            self.__cargaHoraria += disciplina.get_cargaHoraria() 
        else:
            print('Esta disciplina nao pode ser associada a este professor')
 
class Disciplina:
    def __init__(self, nome = '', cargaHoraria = 0, valor = 0.0, professor = None):
        self.__nome  = nome
        self.__cargaHoraria = cargaHoraria
        self.__valor = valor
        self.__professor = professor
 
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
         
    def get_cargaHoraria(self):
        return self.__cargaHoraria
    def set_cargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria
 
    def get_valor(self):
        return self.__valor
    def set_valor(self, valor):
        self.__valor = valor
 
    def get_professor(self):
        return self.__professor
    def set_professor(self, professor):
        self.__professor = professor
 
    def retorna_valor_hora(self):
        return (self.__cargaHoraria/6) * self.__valor
     
p1 = Professor('Joaquim Jose da Silva Xavier', 'joaquim@email.com', '1234', '787-1111')
print(p1.get_nome())
print(p1.retorna_sobrenome())
 
d1 = Disciplina('Matematica 1', 80, 50, p1)
d2 = Disciplina('Estatistica 1', 80, 50, p1)
d3 = Disciplina('Algebra 1', 80, 50, p1)
 
p1.adicionar_disciplina(d1)
p1.adicionar_disciplina(d2)
p1.adicionar_disciplina(d3)
