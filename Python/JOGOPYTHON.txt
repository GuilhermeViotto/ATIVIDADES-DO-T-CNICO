import time
seunom = (input("Qual seu nome?:"))
def inicio():
    
    print("")
    print('Em mundo onde ter magia é comum, todos tem magias, camponeses, soldados, nombreza...todos tem magias...tirando uma pessoa e essa pessoa é...q-que barulho é esse?')
    time.sleep(1)
    print("")
    print('- {}:  AAAAAA SOCORROOO, ALGUÉM ME AJUDAAA (correndo de um URSO de 3 metros)'.format(seunom))
    time.sleep(1)
    
    print("")
    print('-MAGO DO REINO DE LUMIOSE: OQUE VOCE ESTÁ FAZENDO???')
    print("")
    time.sleep(1)
    
    print('-{}:''SÓ ME AJUDAAA'.format(seunom))
    time.sleep(1)
    print("")
    print('-MAGO DO REINO DE LUMIOSE: garoto, oque voce esta fazendo, porque nao derrotou esse urso logo, só ficou gritando...PELO AMOR DE DEUS, SUA VOZ IRRITA')
    time.sleep(1)
    print("")
    print('-{}: foi mal...é que eu nao tenho magia...mas meu sonho é ser a pessoa mais forte de todos os reinos, ser o REI MAGO'.format(seunom))
    time.sleep(1)
    print('-MAGO DO REINO DE LUMIOSE: qual seu nome garoto...?')
    time.sleep(1)
    print("")
    print('Eu me chamo {}'.format(seunom))
    time.sleep(1)
    print("")
    print('Então {}, seguinte, eu acho que consigo te ajudar, porém voce terá que escolher...'.format(seunom))
    time.sleep(1)
    print("")
    escolha_mago()
    
def escolha_mago():
    escolha1 = int(input("\nDIGITE 1 para ir ao reino de Lumiose com o MAGO\nDIGITE 2 para ignorar o convite do MAGO\n{}, qual opção voce escolhe:".format(seunom)))
    time.sleep(1)
    print("")
    if (escolha1 ==1):
         print('Ok {}, então vamos lá!!!'.format(seunom))
  
         mago()
    else:
        print('Ok {}, quem sabe em outra oportunidade, não desista de seus sonhos'.format(seunom))
        print('FINAL MUITO RUIM - Ao recusar as escolhas do mago, seu vilarejo foi atacado, e...voce morreu')
    time.sleep(1)
    
def mago():
    print('você escolheu o mago!!!')
    print("")
    print('CHEGANDO AO REINO LUMIOSE, {} ECONTROU DIVERSOS TIPOS DE MAGOS PODEROSÍSSIMOS(que fizeram uma magia proibida, que fizesse com que ele adquirisse seus poderes mágicos), E ISSO FEZ COM QUE ELE SE JUNTASSE A UM ESQUADRÃO DE MAGOS, E PARTICIPAR DE DIVERSAR MISSÕES PERIGOSAS...'.format(seunom))
    time.sleep(1)
    print("")
    print('-{}: Capitão, voce vai mesmo aceitar essa missão?, ela é muita perigosa'.format(seunom))
    time.sleep(1)
    print("")
    print('Não tenho outra opção {} se nao completarmos essa missão...nosso mundo estará perdido em trevas'.format(seunom))
    time.sleep(1)
    print("")
    print('<<<A CAMINHO DA MISSÃO>>>')
    print("Ao chegar no local da missão encontraram o 1° oponente")
    time.sleep(1)
    combate1()
    
def combate1():
    vitoria = 0
    
    escolha = input('Um inimigo com uma magia INIGUALAVEL tenta enfrentar voce, e ele ja esta carregando sua magia...\n o que voce faz?: \n\n 1:Desferir um ataque poderoso para tentar neutralizar o ataque dele e acerta-lo \n 2:Usar uma magia de boqueio \n 3:Correr do combate \n {},qual opção voce escolhe?:'.format(seunom))
    time.sleep(1)
    
    if(escolha == '1'):
        print('Seu ataque foi muito poderoso e alem de neutralizar, destruiu o seu oponente')
    
        print("")
    
        vitoria+=1
        print('Boa pessoal vamos')
    
        print("")
    elif(escolha == '2'):
        print('FINAL RUIM - Sua defesa falhou, voce estava em estado crítico, e não aguentou os ferimentos . . . e morreu')
    
        print("")
    elif(escolha == '3'):
        print('Correr nao é uma opção para mim!!!')
        print("")
        combate1()
    else:
        print('Voce demorou muito para pensar em reagir e infelizmente morreu.')
    
    
    
    if(vitoria == 0):

        print("")
    else:
        print('{}- Voce pensou que atrapalharia o nosso plano .'.format(seunom))
        print("")
        missao2()
    
    


def missao2():
    vitoria = 1
    escolha2 =  input('Ao avançar, voce encontrou o lider desse oponente, e ele tem UMA MANA SURPREENDENTE, uma mana sombria, voce tenta conversar com ele, porem os conceitos dele não muda \n O QUE VOCE FAZ?: \n 1: Desfiro um ataque com todas minhas forças \n 2: Continuo tentando conversar \n {}, qual opção voce escolhe?: '.format(seunom))
    print("")
    time.sleep(1)
    if(escolha2 == '1'):
        print('Voce desferiu um ataque com todas as suas forças, porém voce nao aguenta mais ficar em pé de tanto casaço')
        print("")
        vitoria +=1
        print('CONSEGUIMOS COMPLETAR A MISSÃO PESSOAL, BOAA')
        print("")
    elif (escolha2 == '2'):
        print('FINAL MEDIANO - Voce tentou continuar a conversar, fez a ação errada e foi retirado da batalha com ferimentos e traumas severos')
        print("")
        missao2()
    else:
        print("")
    
    if(vitoria == 0):
        print('Retorne e escolha novamente . ')
        
    reconhecimento()
    
    
def reconhecimento():
    print('-REI MAGO: PARABENS PESSOAL, VOCES CONSEGUIRAM COMPLETAR A MISSÃO, POREM , NAO CONTAVAM COM A INFORMAÇÃO DE QUE EU . . . EU SOU O VILÃO HAHAHA')
    ilusao()
    
def ilusao():    
    print("")
    escolha3 = input('O Rei Mago usa sua magia de ilusões, fazendo com que você entre em uma ilusão . . . , voce esta diante de dois caminhos, o caminho\n 1: aparenta ser um tunel escuro e perigoso, já o caminho \n 2: é um tunel normal com claridade e muito mais calmo, \n Qual caminho voce escolhe?: ')
    print("")
    time.sleep(1)
    
    if (escolha3 == '1'):
        print(' Voce ecolhe o Túnel escuro, voce avança em direçao, porém antes de completar o percurso, voce da de cara com uma besta de 3 cabeças, voce a derrota, e consegue sair da ilusão')
        print("")
        time.sleep(1)
        print("")
        finalmtbom()
    elif (escolha3 == '2') :
        print('FINAL BOM - Voce escolheu o tunel mais calmo, da de encontro com um calabouço infinito, cai nele, e fica em uma ilusão infinita, vivendo as coisas que mais gosta . . .')
    
def finalmtbom():
    escolha4 = input('FINAL MUITO BOM - Ao sair da ilusão, voce lutou contra o rei mago, mesmo ele tendo uma força imensurável, voce juntou forças com seu capitão e seu esquadrão, e conseguiram derrotar o Rei Mago, sendo reconhecido por todos, como o salvador do reino de Lumiose ')
    fim_jogo()
def fim_jogo():
    print('PARABENS VOCE ACABOU O JOGO')
 
inicio()

    



















