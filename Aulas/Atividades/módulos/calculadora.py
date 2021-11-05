#Criação das variáveis para um cálculo simples
def soma_sub(n1, n2, calculo_soma, calculo_sub):
    n1 = float(input("Digite um número:"))
    n2 = float(input("Digite outro número:"))
    calculo_soma = n1+n2
    calculo_sub = n1-n2

    soma_sub(n1,n2,calculo_soma,calculo_sub)

#Criando situações
    print("Os números digitados foram:", n1, "e", n2,'\n')
def escolha_calculo(possibilidades_lista, escolha, possibilidades):
    possibilidades_lista = [('soma','Soma','adição','Adição', 'adicao', 'Mais', 'mais','Adicao','Subtração','subtração', 'menos', 'Menos')]
    possibilidades = dict(possibilidades_lista)
    escolha = print(possibilidades_lista.get(input("Digite o tipo de cálculo: ")))
    
     
    
    if(escolha<=[7]):
        print("O resultado é:", calculo_soma)