nomeList = []
idadeList = []
sexoOption = ('Feminino', 'Masculino', 'Outro')
sexoList = []

# Registro de Cliente
print("---Registro---")
try:
    quantidadeUsuario = input("Número de usuários a serem criados (Limite máximo de 10 usuários): ")
    quantidadeUsuario = int(quantidadeUsuario)
    if quantidadeUsuario > 10 or quantidadeUsuario <= 0:
        print("Quantidade inválida")
        quantidadeUsuario = 0 
except ValueError:
    print("Entrada inválida. Por favor, insira um número válido.")
    quantidadeUsuario = 0  

#Criação do usuário
for i in range(quantidadeUsuario):
    print("----------")
    # nomeUsuario
    nomeUsuario = input(f"Nome do usuário: ")
    nomeList.append(nomeUsuario)
    
    # idadeUsuario
    while True:
        idadeUsuario = input(f"Idade do usuário: ")
        try:
            idadeUsuario = int(idadeUsuario)
            if idadeUsuario < 18:
                print("Idade mínima 18")
            elif idadeUsuario > 115:
                print("Idade máxima 115")
            else:
                idadeList.append(idadeUsuario)
                break
        except ValueError:
            print("Entrada inválida.")

    # sexoUsuario
    while True:
        sexoUsuario = input(f"Sexo do usuário (Feminino, Masculino, Outro): ").capitalize()
        if sexoUsuario in sexoOption:
            if sexoUsuario == 'Outro':
                identificacao = input(f"Identificação: ").capitalize()
                sexoUsuario = identificacao
            sexoList.append(sexoUsuario)
            break
        else:
            print("Opção inválida. Escolha entre Feminino, Masculino, ou Outro.")

# Dicionário
baseUsuarioDict = {
    "nome": nomeList,
    "idade": idadeList,
    "sexo": sexoList
}

# Função de Visualização dos Registros
def visualizacaoRegistros():
    print("----------")
    print("Registros Criados")
    for i, (nome, idade, sexo) in enumerate(zip(baseUsuarioDict["nome"], baseUsuarioDict["idade"], baseUsuarioDict["sexo"])):
        print(f"Registro {i + 1}: Nome: {nome}, Idade: {idade}, Sexo: {sexo}")

if quantidadeUsuario > 0 and quantidadeUsuario <= 10:
    visualizacaoRegistros()