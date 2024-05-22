def recomendar_plano(consumo):
  essencial_fibra = 'Plano Essencial Fibra - 50Mbps'
  prata_fibra = 'Plano Prata Fibra - 100Mbps'
  premium_fibra = 'Plano Premium Fibra - 300Mbps'
  
  if consumo <= 10:
    print(f'Seu consumo mensal é de {consumo} GB.\nO plano ideal para você é o {essencial_fibra}.')
  elif consumo <= 20:
    print(f'Seu consumo mensal é de {consumo} GB.\nO plano ideal para você é o {prata_fibra}.')
  else:
    print(f'Seu consumo mensal é de {consumo} GB.\nO plano idela para você é o {premium_fibra}.')

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input('Informe seu consumo mensal de internet:\n'))
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
recomendar_plano(consumo)