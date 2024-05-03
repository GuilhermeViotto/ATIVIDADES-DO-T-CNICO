def calculadora():
    
    oper = (input("Operação:\n+ (ADIÇÃO)\n- (SUBTRAÇÃO)\n* (MULTIPLICAÇÃO)\n/ (DIVISÃO)\nQual voce escolhe: "))
    if oper != '+' and oper != '-' and oper != '*' and oper != '/':
        print('Operação inválida, digite um valor válido')
        calculadora()
    try:
        n1 = float(input("Digite o primeiro número:"))
        n2 = float(input("Digite o segundo número:"))
    except ValueError:
        print('Numero Inválido, digite valores válidos')
        calculadora()
        

        
    

    if oper == "+":
        soma(n1, n2)
        
    elif oper == "-":
        subtracao(n1, n2)
        
    elif oper == "*":
        mult(n1, n2)
        
    elif oper == "/":
        divisão(n1, n2)
        
def soma(n1, n2):
    resultado = n1 + n2
    print('A soma de seus numeros é:',resultado)
    
    opdnv()
    
def opdnv():
    dnv = input('Deseja fazer outra operação?\nDigite S para Sim: \nN para Não:')
    print("")
    if dnv.upper() == 'S':
        print('Escolha os valores de sua nova operação:')
        calculadora()
        
    else :
        print('Sua operação foi concluída')
        fim_oper()
def subtracao(n1, n2):
    resultado = n1 - n2
    print('A subtração de seus numeros é:', resultado)
    print("")
    opdnv()
    
def mult(n1, n2):
    resultado = n1 * n2
    print('A multiplicação de seus numeros é:', resultado)
    print("")
    opdnv()
    
def divisão(n1, n2):
    resultado = n1 / n2
    print('A divisão de seus numeros é:', resultado)
    print("")
    opdnv()
    

    
    
def fim_oper():
    print('acabou ')
    
calculadora()

