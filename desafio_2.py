# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
# TODO: Solicite o item e armazena na variável "item":

# TODO: Adicione o item à lista "itens":
# TODO: Crie um loop para solicita os itens ao usuário:
itens = []

for i in range(0,3):
  equipamentos = input('Informe o equipamento: ')
  itens.append(equipamentos)
# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")