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

# Criar Inputs

# email_input = input("Qual o seu email? ")

# Utilizado o int para transformar string em number para ser realizado o calculo (utilizar float para números com casas decimais)

#renda_input = int(input("Qual sua renda mensal? "))

#print (f"O seu email é: {email_input} e a sua renda anual é {renda_input * 12}")

# Listas

valores = [100,52,365,159,103,86,35,42]

soma_lista = sum(valores)

print(f"A soma dos valores da lista resulta em: {soma_lista}")

qtd_valores_lista = len(valores)

print(f"A quantidade de valores da lista é igual a: {qtd_valores_lista} valores")

max_valor_lista = max(valores)

print(f"O maior valor da lista é: {max_valor_lista}")

min_valor_lista = min(valores)

print(f"O menor valor da lista é: {min_valor_lista}")

prim_val_lista = valores[0]

print(f"O primeiro valor da lista é: {prim_val_lista}")

ult_val_lista = valores[-1]

print(f"O ultimo valor da lista é: {ult_val_lista}")

# Verificar se um item existe na lista

lista_produtos = ["Iphone","Ipad","Macbook","Airtag"]

produto_novo = "Vision Pro"

print_time = 1

if produto_novo in lista_produtos:
    print(f"O produto existe na lista. Print {print_time}")
else:
    print(f"O produto não existe na lista. Print {print_time}")

print_time = 2

# Adicionar item na lista

lista_produtos.append(produto_novo)

if produto_novo in lista_produtos:
    print(f"O produto existe na lista. Print {print_time}")
else:
    print(f"O produto não existe na lista. Print {print_time}")

print_time = 3

# Remover item da lista (Diferença de remove e pop)

lista_produtos.remove(produto_novo)

if produto_novo in lista_produtos:
    print(f"O produto existe na lista. Print {print_time}")
else:
    print(f"O produto não existe na lista. Print {print_time}")

print_time = 4

lista_produtos.append(produto_novo)

if produto_novo in lista_produtos:
    print(f"O produto existe na lista. Print {print_time}")
else:
    print(f"O produto não existe na lista. Print {print_time}")

print_time = 5

lista_produtos.pop(-1)

if produto_novo in lista_produtos:
    print(f"O produto existe na lista. Print {print_time}")
else:
    print(f"O produto não existe na lista. Print {print_time}")

# Editar itens na lista

precos_produtos = [1000,8000,15000,300]

print(precos_produtos)

precos_produtos[0] = 6200

print(precos_produtos)

# Contar quantas vezes um item aparece na lista

lista_produtos = lista_produtos = ["Iphone","Ipad","Macbook","Airtag","Airtag","Iphone","Ipad","Airtag","Airtag","Iphone"]

print(lista_produtos)

produto_conta = "Iphone"

qtd_produto = int(lista_produtos.count(produto_conta))

if qtd_produto > 1:
    print(f"Há {qtd_produto} {produto_conta}s no estoque")
elif qtd_produto > 0 and qtd_produto < 2:
    print(f"Há {qtd_produto} {produto_conta} no estoque")
else:
    print(f"O produto {produto_conta} não existe na lista")

# Ordenar lista

lista_produtos.sort()

print("Lista em ordem crescente:")

print(lista_produtos)

lista_produtos.sort(reverse=True)

print("Lista em ordem decrescente:")

print(lista_produtos)
