'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q01():
    print('João Paulo')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q02():
    print(30 * 27)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q03():
    media = (5+ 8+ 12)/3
    print(media)

#4. Faça um programa que leia e imprima um número inteiro.
def q04():
    numero=int(input("Digite um numero inteiro:"))
    print(numero)

#5. Faça um programa que leia dois números reais e os imprima.
def q05():
    num1 = float(input('Digite o primeiro numero real: '))
    num2 = float(input('Digite o segundo numero real: '))
    print(num1,num2)   

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q06():
    num=int(input('Digite um numero inteiro'))
    print(f' Antecessor: { num-1}')
    print(f' Sucessor:{num+1}')

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q07():
    nome= input('Nome: ')
    endereço= input('Endereço: ')
    telefone= input('Telefone: ')
    texto= f'''
      Nome: {nome}
      Endereço:{endereço}
      Telefone: {telefone}
      '''
    print(texto)
      
#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q08():
    num1= int(input(' Num1: '))
    num2= int(input(' Num2: '))
    print(f'{num1}-{num2}= {num1-num2}')
    

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q09():
    num=float(input("Digite um numero real"))
    print(f'{num/4}')



#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1=float(input("Digite um numero real"))
    num2=float(input("Digite o segundo numero real"))
    num3=float(input("Digite o terceiro numero real"))
    print(f'{(num1+num2+num3)/3}')
    


#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    num1= float(input('num1:'))
    num2=float(input('num2:'))
    print(f'{num1}+{num2} = {num1}+{num2}')
    print(f'{num1}-{num2} = {num1}-{num2}')
    print(f'{num1}*{num2} = {num1}*{num2}')
    print(f'{num1}/{num2} = {num1}/{num2}')
    


#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    num=float(input("Digite um numero real"))
    print(f"resultado foi de:{num**2} ")
   

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    saldo = float(input('Saldo:R$'))
    novo_saldo = (saldo*1.02)
    print(f"esse é o {saldo},e esse é o valor final{novo_saldo}")
    

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).
def q14():
    base = float(input('base*2')) 
    altura = float(input(altura*2))
    perimetro = float((base*2 + altura*2))
    area = float(input(base * altura))
    print(f'Esse é o valor do {perimetro}, e esse é o valor da {area}')   

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
    valor_produto= float(input('valor do produto: R$'))
    percentual_desconto=float(input('percentual_desconto: '))
    valor_desconto=round(valor_produto*percentual_desconto/100, 2)
    valor_produto_desconto=valor_produto-valor_desconto
    resultado=f'''
    valor do Produto: R${valor_produto}
    valor do desconto({percentual_desconto}%): R$ {valor_desconto}
    valor final do produto: R$ {valor_produto_desconto}
    '''
    print(resultado)


#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida em horas
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.

#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será

questao = int(input('Questão a executar: '))
eval(f'q{questao}()')