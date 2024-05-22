# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
# TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
# TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.

# Imprime o resultado:
import re

def validate_numero_telefone(phone_number):
    if re.match(pattern, phone_number):  

        return print(f'Número de telefone válido.')
        # TODO: Agora crie um return, para retornar que o número de telefone é válido:
    else:
        return print(f'Número de telefone inválido.')
       # TODO: Crie um else e return, caso não o número de telefone seja inválido:
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  
pattern = '(\([0-9]{2}\)) ([9]{1})([0-9]{4})-([0-9]{4})'
validate_numero_telefone(phone_number)
# print(result)