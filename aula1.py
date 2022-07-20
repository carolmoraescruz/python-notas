string = ("Hello world!")

print(string)

print(string[:5])

string2 = '0 0 0 0 0 0 0 0 0 0'
print(string2[0::2])
print(string2[:10:2])
print(string2[:9])

string3 = "Digital House"
print(string3[::-1])

nome_pessoa = input("Digite o seu nome: ")
print(nome_pessoa)

comida = input("Qual sua comida preferida: ")
print(f"Sua comida preferida é {comida}")

palavra = input("Digite uma palavra: ")
print(f"Olá estranho, você digitou {palavra}")

nome_usuario = input("Digite seu nome: ")
letra = nome_usuario[0]
print(f"Olá, a primeira letra do seu nome é {letra}")

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_padronizado = nome[0].upper() + nome[1::].lower()
sobrenome_padronizado = sobrenome[0].upper() + sobrenome[1::].lower()
print(f"Olá, {nome_padronizado} {sobrenome_padronizado}")

# Segunda opção

nome_completo = input("Digite seu nome completo: ")
nome_completo_padronizado = nome_completo.title()
print(f"{nome_completo_padronizado}")

info = input("Digite pelo menos dois nomes: ")
nomes = info.split()
if "Pedrinho" in nomes:
    print("Acorda!")

print(10*"-")
