#1 - Liste uma sequência de 10 números do maior para o menor.
for numero in range(10 , 1 , -1):
    print(numero)



#2 - liste uma sequência numérica que começa em um valor inserido pelo usuário e acaba em um valor escolhido pelo usuário
n1 = int(input("Insira seu número:"))
n2 = int(input("Informe seu segundo número:"))

if (n1 < n2):  
    while n1 <= n2:
        print(n1)
        n1 +=1
else:
    for n2 in range(n1,n2, -1):
        print(n2)



#3 -Solicite um número ao usuário e imprima a tabuada desse número, de 1 a 10
n1 = int(input("Digite seu número:"))

for i in range(1,11):
        print('{} x {} = {}'.format(n1,i,n1*i))



#4 -Solicite dois números ao usuário e verifique quantos números pares ou ímpares existem entre esses dois números .
n1 = int(input("Solicite o primeiro número:"))
n2 = int(input("Solicite o segundo número:"))
par = 0
impar = 0
for i in range(n1, n2+1):
    if(i%2 ==0):
        par+=1
        print(i)
    else:
        impar+=1
        print(i)
        
        
        
        
print('Entre seus números existe a quantidade de {} números pares e {} de números impares'.format(par , impar))
        

#5 - Solicite um número inteiro positivo N ao usuário e calcule a soma dos primeiros N números naturais.
soma = 0
n = int(input("Insira um número positivo:"))

for i in range(1,n +1):
    soma+=i
    print(i)
    
print(soma)




#6 - Solicite ao usuário a quantidade de notas que ele deseja inserir, em seguida, solicite essas notas e calcule a média.
soma = 0 
qntd = int(input("Quanta notas voce deseja inserir:"))

for i in range(qntd):
    print(i)
    not1 = int(input("Informe suas notas:"))
    soma+=not1
    
media = soma/qntd
print('Sua média é de: {}'.format(media))
    




#7 - Solicite um número inteiro positivo ao usuário e calcule o fatorial desse número.
soma = 1
n = int(input("Insira um número positivo:"))

for i in range(1,n +1):
    soma*=i
    print(i)
    
print(soma)





#8 -Desenvolva um programa em Python que permita ao usuário escolher um número e gere a tabuada desse número até um limite especificado pelo próprio usuário.
num = int(input("Digite seu número:"))
fin = int(input("Digite o limite de sua tabuada:"))
for i in range(1,fin+1):
    print('{} x {} = {}'.format(num,i,num*i))




#9 - Desenvolva um programa em Python que solicite ao usuário um número inteiro. O programa deverá então exibir a tabuada de multiplicação até o número escolhido pelo usuário, fazendo as multiplicações de 1 até 10.
num = int(input("Digite seu número:"))

for i in range(1,num+1):
    print('Essa é a tabuada do {}'.format(i))
    print("")
    for y in range(1,11):
        print('{} x {} = {}'.format(i,y,i*y))





#10 - Crie um programa em python que faça um triângulo da altura que o usuário escolher(Desafio)

tri = int(input("Digite a altura do triângulo que deseja:"))
     
for i in range(tri):
    print(" "*(tri- i)+"*"*(2*i+1))
    

        
   






