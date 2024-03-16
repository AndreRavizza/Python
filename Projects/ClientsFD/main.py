class main:
    pass

print("teste")

from cliente import Cliente

from conta import conta

c1 = Cliente("João","114444-2222")
conta = conta(c1.nome,6565,0)

print(conta.titular," Numero: ",conta.numero, "Seu saldo: ", conta.saldo)
