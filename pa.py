#Anderson e Felipe
class Registro:
    def __init__(self, nome, idade, endereço):
        self.nome = nome
        self.idade = idade
        self.endereço = endereço

    def registrar_pessoa(self):
        self.nome =(input("Digite seu nome: "))
        self.idade =(input("Digite sua idade: "))
        self.endereço = (input("Didigte o seu endereço: "))
        return[self.nome, self.idade, self.endereço]


Registro.registrar_pessoa()
print("IDE é o ambiente no qual você digita seus codigos de programação")
print("Dono do github e Git é a Microsoft")
print("Versionamento de códigos é importante pois ele ajuda a armazenar e editar os códigos o separando em partes. ")