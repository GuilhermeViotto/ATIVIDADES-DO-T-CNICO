ATIVIDADE 1

#1) Calcular a Média de Três Números
numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))
numero3 = float(input("Digite o terceiro número:"))

media = (numero1 + numero2 + numero3)/3;
print ("Sua média é de:",media)

#2) Calcular a Soma de Dois Números:
numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))
soma = (numero1 + numero2)
print("Sua soma é de:",soma)


#3) Converter Idade para Dias:
idade = float(input("Digite sua idade:"))
diasdevida  = (idade * 365)
print ("Você tem ", diasdevida , " dias de vida ")

#4) Calcular o Quadrado de um Número:
numero = float(input("Digite o seu número:"))
quadrado = (numero * numero)
print ("O quadrado do seu número é: ", quadrado)

#5) Verificar se um Número é Par ou Ímpar:
numero = float(input("Digite seu número:"))
if(numero %2 ==0):
    print("Seu número é par")
else:
    print("Seu númerpo é impar")

#6) Faça um programa que converta metros em centímetros.
metro = float (input("Digite seu metro:"))
centimetro = metro * 100
print("Seu metro em centímetros é:", centimetro)


#7)Faça um programa que pergunte quanto você ganha por hora, quantas horas você tem trabalhada no mês e mostre quanto você ganharia em 3 meses.
gnhphr = float(input("Informe o quanto vc ganha por hora:"))
horas = float(input("Informe as horas trabalhadas:"))

preçode3mss = (gnhphr * horas) * 3
print("Daqui 3 meses vc ganharia:",preçode3mss)


#8)Faça um programa que pegue o raio de um círculo e calcule sua área.
raio = float(input("Informe o raio do circulo:"))
area = 3.14 * (raio * raio)
print("A area do circulo é :", area)


#9)Faça um programa que calcule a área de um quadrado.

lado = float(input("Informe seu lado:"))
quadrado = lado **2
print("Sua area do quadrado é de:",quadrado)


#10)Faça um programa que recebe o salário total de alguém e mostra como seria esse salário com um aumento de 5%, 15% e 30%.
salario = float(input("Informe seu salario:"))
aumento = salario * 0.5 , salario * 1.5 , salario * 1.3
print ("Seu suposto salario seria de:", aumento)

#11)Faça um programa que recebe nome, idade e apelido de alguém e devolve uma frase de boas vindas.
nome = (input("Digite seu nome:"))
idade = (input("Digite sua idade:"))
apelido = (input("Digite seu apelido:"))
print ("Bem Vindo ", apelido)




ATIVIDADE 2 


#1 Exiba o maior número entre dois valores.
n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))

if n1 > n2:
    print ("O maior número é o ",n1)
else:
    print ("O maior número é o ", n2)


#2 Exiba o menor número entre dois valores.
n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))

if n1 < n2:
    print ("O menor número é o ",n1)
else:
 print ("O menor número é o ", n2)


#3 Agora crie uma condição adicional dizendo se ambos os números forem iguais.
n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))

if (n1 > n2):
    print("Os numeros não são iguais")
    
elif (n1 == n2):
    print("Os numeros são iguais")
    
else:
    print("Os numeros não são iguais")


#4 Peça o nome e salário de dois funcionários, traga qual ganha mais, e quanto ele ganha mais que o outro funcionário.
func1 = input("Digite o nome do primeiro funcionario:")
func2 = input("Digite o nome do segundo funcioario:")
salario1 = float(input("Digite o salario do primeiro funcionario:"))
salario2 = float(input("Digite o salario do segundo funcionario:"))

if (salario1 > salario2):
    print("o salario do primeiro funcionario é maior, com a diferença de", salario1- salario2, "reais")

else:
    print("o salario do segundo funcionario é maior")

#5 Faça um programa que diga o imc e se a pessoa está abaixo do peso (menos que 18,5) ,com peso ideal(entre 18,5 e 24,9 ) ou acima do peso (maior que 24,9).

peso = float(input("Me informe seu peso:"))
altura = float(input("Me informe sua altura:"))
imc = peso / (altura * altura)

if imc <18.5:
    print("Voce está abaixo do seu peso ideal")
    
elif imc >=18.5 and imc <=24.9:
    print("Voce está com o peso ideal")
    
else:
    print("Voce está acima do peso irmão")
#6  Faça um programa que verifique se a pessoa é maior de idade e do sexo feminino.
idade = float(input("Quantos anos voce tem?:"))
sexo = (input("Qual o seu sexo?: Digite (F) para feminino ou (M) para falso:"))

if idade <18:
    print("Voce nao pode pois, é menor de idade")
elif idade >=18 and sexo.upper()=="F":
    print("Seu acesso foi permitido, pois voce é mulher e é maior de idade")
elif idade >18 and sexo.upper() =="M":
    print("Voce nao pode, pois so precisamos de mulheres no cargo")
else :
    print("Voce nao atende aos requisitos necessários")


#7 Organiza três números do maior para o menor.
n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero:"))
n3 = float(input("Digite o terceiro numero:"))

if n1 > n2 and n2 > n3:
    print('A ordem é ', n1 ,',' , n2 ,',', n3 )
elif n1 > n3 and n3 > n2:
    print('A ordem é', n1 ,',', n3 ,',', n2)
elif n2 > n1 and n1 > n3:
    print('A ordem é ', n2 ,',', n1, ',',n3)
elif n2 > n3 and n3 > n1:
    print('A ordem é', n2,',', n3, ',', n1)
elif n3 > n1 and n1 > n2:
    print('A ordem é', n3,',' , n1 ,',' , n2)
else :
    print('A ordem é', n3 ,',', n2 ,',', n1)


#8 Some dois números, se o valor resultante for positivo e par, devolva “+par”, se for positivo mas ímpar devolva”+ímpar”, siga a mesma lógica para números negativos.

n1 = float(input("Informe o primeiro numero:"))
n2 = float(input("Informe o segundo numero:"))
soma = (n1 + n2) 
if soma > 0 and soma %2 ==0:
    print('o numero {} e o numero {} resultou em {} +par'.format(n1 , n2 , soma))
elif soma >0 and soma %2 ==1:
    print('o numero {} e o numero {} resultou em {} +impar'.format (n1 , n2 , soma))
elif soma <0 and soma %2 ==0:
    print('o numero {} e o numero {} resultou em {} -par'.format (n1 , n2 , soma))
elif soma <0 and soma %2 ==1:
    print('o numero {} e o numero {} resultou em {} -impar'.format (n1 , n2 , soma))

#9 Some dois valores e devolva a mensagem “É isso aí” se a soma resultar em 40 ou entre 25 e 33. E devolva as opções possíveis
n1 = float(input("Informe o primeiro numero:"))
n2 = float(input("Informe o segundo numero:"))
soma = (n1 + n2)
if (soma == 40 or soma >= 25 and soma <= 33):
    print('É ISSO AI')
else:
    print('A soma dos numeros nao atende aos requisitos necessários')


#10 Verifique se alguém é maior de idade para entrar em um bar no brasil + 18 ou nos estados unidos +21 e devolva as opções cabíveis. 
idade = float(input("Me informe sua idade:"))
if idade >=21:
    print('Sua entrada é permitida nos bares dos 2 países')
elif idade >=18:
    print('Sua entrada é permitida nos bares do Brasil, e nao nos bares dos Estados Unidos')
else:
    ('Sua entrada nao é permititda nos bares de nenhum dos 2 paises')


#11 Um parque aceita que qualquer um com mais de 1,60 e 16 anos vá nos brinquedos, agora se você tiver 1,50 e estiver acompanhado também é permitido, porém se tiver menos que 1,50 e for maior de idade terá que assinar um termo para usar os brinquedos, caso seja menor que 1,50 e não for maior de idade não poderá usar os brinquedos mesmo que esteja acompanhado, mas lhe será recomendado passeios menos perigosos. Crie um código com todas as possibilidades
altura = float(input("Informe sua altura:"))
idade = float(input("Informe sua idade:"))
acomp = (input("Voce esta acompanhado, diga (S) para SIM ou (N) para NÃO:"))
if altura >1.60 and idade >=16:
    print('Voce pode ir aos brinquedos')
elif altura <=1.50 and acomp.upper()== "S":
    print('Sua entrada foi permitida, pois esta acompanhada, porem sua altura nao é permitida')
elif altura <1.50 and idade >=18:
    print('Sua entrada foi permtidia, porem terá que assinar um termo para poder andar nos brinquedos')
elif altura <1.50 and idade <18:
    print('Sua entrada nao foi permitida mesmo que esteja acompanhada, sinto muito')


