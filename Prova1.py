# String
nome = input('Digite o seu nome: ')
print(f'Seu nome é:', nome)

# Inteiros
idade = int(input("Digite a sua idade: "))
print("Sua idade é:", idade)

# Float
altura = float(input("Digite a sua altura: "))
print("Sua altura é:", altura)

# Solicitação ao usuário de 4 notas, em seguida calcule a média e informe a média para o usuário:

nota1 = float(input('Digite a nota do 1º Semestre: '))
nota2 = float(input('Digite a nota do 2º Semestre: '))
nota3 = float(input('Digite a nota do 3º Semestre: '))
nota4 = float(input('Digite a nota do 4º Semestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média do ano letivo é: {media}")