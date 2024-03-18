class main:
    pass

# utilizando uma função

from defs import Calc

c02 = Calc(1, 3)

print(c02.result)

# Alimentando e manipulando variáveis

faturamento = 1123452
despesa = 689251
lucro = faturamento - despesa
margem_lucro = lucro / faturamento

# Formas de inserir variáveis na string

print("O faturamento foi de: {}, as despesas foram de {} e o lucro foi de {}".format(faturamento,despesa,round(lucro,2)))

print(f"O faturamento foi de: R$ {faturamento}, as despesas foram de R$ {despesa} e o lucro foi de R$ {lucro} e a margem foi de {margem_lucro}")

# Formatando valores para cada decimal. f = float % = porcentagem:

print(f"O faturamento foi de: R$ {faturamento:.2f}, as despesas foram de R$ {despesa:.2f} e o lucro foi de R$ {lucro:.2f} e a margem foi de {margem_lucro:.0%}")

# Formatar texto para maíusculo ou minúsculo:

email_cliente = "EmailQualquer@OUTLOOK.COM"

email_cliente = email_cliente.upper()
print(f"O e-mail do cliente em maiúsculo é: {email_cliente}")

email_cliente = email_cliente.lower()
print(f"O e-mail do cliente em minusculo é: {email_cliente}")

# Localizar caractere em um texto:

print(email_cliente.find("@"))

# Verificar se um e-mail é valido com base na existência de um caractere:

if email_cliente.find("@") == -1:
    print(f"O e-mail {email_cliente} é inválido")
else:
    print(f"O e-mail {email_cliente} é válido")

# Contando caracteres:

print(f"O e-mail {email_cliente} possui {len(email_cliente)- 1} caracteres")

# Selecionado partes específicas de um texto:

print(f"O primeiro caracter do e-mail é {email_cliente[0]} e o ultimo caracter é {email_cliente[-1]}")

print(f"Até o caractere 5 do e-mail temos isso: {email_cliente[:5]}")

print(f"Do caractere 2 até o caractere 5 do e-mail temos isso: {email_cliente[2:5]}")

print(f"A partir do caractere 5 do e-mail temos isso: {email_cliente[5:]}")

# Substituir parte do texto por algo:

novo_email = email_cliente.replace("outlook","gmail")

print(f"O e-mail antigo era {email_cliente} e agora o email é {novo_email}")

# Formatar texto com primeira letra maíuscula (Diferença entre o capitalize e o title):

nome_cliente = "andre ravizza"

print(nome_cliente.capitalize())
print(nome_cliente.title())

# Utilizando o find para localizar o domínio do e-mail:

dominio_email_cliente = email_cliente[email_cliente.find("@"):]

print(f"O domínio do e-mail do cliente é: {dominio_email_cliente}")

# Separando o primeiro nome e o sobrenome de um texto:

espaco_nome_cliente = nome_cliente.find(" ")

print(f"O primeiro nome do cliente é: {nome_cliente[:espaco_nome_cliente]} e o sobrenome é {nome_cliente[espaco_nome_cliente+1:]}")
