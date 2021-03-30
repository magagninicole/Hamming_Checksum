import tkinter as tk
from random import randint
from random import seed
import numpy as np

#Alunos: João Vitor Specht Kogut, Nicole Magagnin
#Código de aluno usado: 6462340, soma dos útimos 3 dígitos = 7


def start():

    def soma_of(lista): #Soma caso haja overflow
        palavra1 = lista
        palavra2 = [0,0,0,0,0,0,1]
        of = False
        soma = []

        for i in range( len(palavra1)-1, -1, -1):#loop da direita para a esquerda
            estado = palavra1[i] + palavra2[i]  #O estado é igual a soma dos bits da posição da palavra
            if(of == True): # Se houver overflow 
                estado = estado + 1 #Estado é acrescentado um bit, o "vai um"
                of = False #Overflow torna-se false

            if(estado == 0): #Se a soma das palavras é de 0+0, insere 0
                soma.insert(0, 0)
                
            if(estado == 1): #Se a soma é de 0+1, insere 1
                soma.insert(0, 1)

            if(estado == 2): #Se a soma é de 1+1, insere 0 e vai para o overflow
                soma.insert(0, 0)
                of = True

            if(estado == 3): #Se a soma é 1+1+1 devido ao overflow anterior, insere um e overflow = true
                soma.insert(0, 1)
                of = True 

        return soma



    def calcula_checkSum():
        # soma 1° com 2° palavra
        # caso tenha overflow = soma um bit no mais a direita
        # fazer o mesmo com a 3° palavra
        # fazer complemento de 2 com o resultado
        # Envia EDC + as 3 palavras
        # Somar tudo

        palavra1_str = list( i_palavra1.get() )
        palavra2_str = list( i_palavra2.get() )
        palavra3_str = list( i_palavra3.get() )
        palavra1 = []
        palavra2 = []
        palavra3 = []

        if (len(palavra1_str) == 7 and len(palavra2_str) ==7 and len(palavra3_str)==7):
            l_tamanho['text'] = "TAMANHO DA PALAVRA CORRETO"
            for i in range( len( palavra1_str ) ):
                palavra1.insert( len(palavra1), int(palavra1_str[i])  )
                palavra2.insert( len(palavra2), int(palavra2_str[i])  )
                palavra3.insert( len(palavra3), int(palavra3_str[i])  )

        

            soma_1e2 = []
            of = False
            
            for i in range( len(palavra1)-1, -1, -1): #Loop decrementando para que a soma seja resolvida da direita para a esquerda
                estado = palavra1[i] + palavra2[i]

                if(of == True): #Caso overflow "vai um"
                    estado = estado + 1 #Estado é acrescentado um bit, o "vai um"
                    of = False

                if(estado == 0):#Se a soma das palavras é de 0+0, insere 0
                    soma_1e2.insert(0, 0)
                    
                if(estado == 1): #Se a soma é de 0+1, insere 1
                    soma_1e2.insert(0, 1)

                if(estado == 2):#Se a soma é de 1+1, insere 0 e vai para o overflow
                    soma_1e2.insert(0, 0)
                    of = True

                if(estado == 3):#Se a soma é 1+1+1 devido ao overflow anterior, insere um e overflow = true
                    soma_1e2.insert(0, 1)
                    of = True 

                if( i == 0 and of == True): #Caso overflow termine em true, é chamada a função overflow enviando as palavras,
                    soma_1e2 = soma_of(soma_1e2)#Assim é realizada a soma do overflow, somando 1 ao bit menos significativo
                    of = False

            
            soma_Re3 = []
            of = False
            
            for i in range( len(palavra1)-1, -1, -1): #Mesmo processo para somar a segunda a 3a palavra
                estado = soma_1e2[i] + palavra3[i]

                if(of == True):
                    estado = estado + 1
                    of = False

                if(estado == 0):
                    soma_Re3.insert(0, 0)
                    
                if(estado == 1):
                    soma_Re3.insert(0, 1)

                if(estado == 2):
                    soma_Re3.insert(0, 0)
                    of = True

                if(estado == 3):
                    soma_Re3.insert(0, 1)
                    of = True 

                if( i == 0 and of == True):
                    soma_Re3 = soma_of(soma_Re3)
                    of = False


            #complemento_de_2 para gerar o EDC
            for i in range( len( soma_Re3 ) ):
                if(soma_Re3[i] == 1):
                    soma_Re3[i] = 0
                else:
                    soma_Re3[i] = 1
            
            
            EDC = soma_Re3
            EDC_str = ""
            for i in range(len(EDC)):
                EDC_str = EDC_str + str(EDC[i])

            l_result_edc['text'] = EDC_str

        else:
            l_tamanho['text'] = "TAMANHO DA PALAVRA INCORRETO"
        

    def Transmite(): #Essa função gera um resultado de transmissão aleatório, podendo ou não gerar erros ao transmitir

        ran = np.random.randint(0,35) #Random para a posição entre 0 e 35
        palavra1_str = list( i_palavra1.get() )
        palavra2_str = list( i_palavra2.get() )
        palavra3_str = list( i_palavra3.get() )
        palavra1 = []
        palavra2 = []
        palavra3 = []

        for i in range( len( palavra1_str ) ):  
            palavra1.insert( len(palavra1), int(palavra1_str[i])  )
            palavra2.insert( len(palavra2), int(palavra2_str[i])  )
            palavra3.insert( len(palavra3), int(palavra3_str[i])  )

        if(ran <= 6): #Caso o valor aleatório gerado esteja na primeira palavra, é "errada" a posição da mesma
            if(palavra1[ran] == 1): #Correspondente ao valor aleatório gerada, o bit é invertido
                palavra1[ran] = 0
            else:
                palavra1[ran] = 1

        if(ran > 6 and ran<14): #O mesmo para a segunda palavra
            if(palavra2[ran-7] == 1):
                palavra2[ran-7] = 0
            else:
                palavra2[ran-7] = 1

        if(ran > 13 and ran < 22): #E terceira
            if(palavra3[ran-14] == 1):
                palavra3[ran-14] = 0
            else:
                palavra3[ran-14] = 1 #Quanto a outros valores gerados randomicamente entre 22 e 35, as palavras não são
                #alteradas, não gerando erros

        palavra1_err = ""
        palavra2_err = ""
        palavra3_err = ""

        for i in range(len(palavra1)):
            palavra1_err = palavra1_err + str(palavra1[i])
            palavra2_err = palavra2_err + str(palavra2[i])
            palavra3_err = palavra3_err + str(palavra3[i])
        
        
        l_palavra_errada1['text'] = palavra1_err
        l_palavra_errada2['text'] = palavra2_err
        l_palavra_errada3['text'] = palavra3_err
        


    def checka(): #Função checa se existem erros nas mensagens
        palavra1_str = list( l_palavra_errada1['text'] )
        palavra2_str = list( l_palavra_errada2['text'] )
        palavra3_str = list( l_palavra_errada3['text'] )
        EDC_str = list( l_result_edc['text'] )
        
        EDC = []
        palavra1 = []
        palavra2 = []
        palavra3 = []


        for i in range( len( palavra1_str ) ):
            palavra1.insert( len(palavra1), int(palavra1_str[i])  )
            palavra2.insert( len(palavra2), int(palavra2_str[i])  )
            palavra3.insert( len(palavra3), int(palavra3_str[i])  )
            EDC.insert (len(EDC), int(EDC_str[i]) )

        soma_1e2 = [] 
        of = False
        
        for i in range( len(palavra1)-1, -1, -1): #São somadas as palavras 1 e 2 recebidas, com as devidas checagens de overflow
            estado = palavra1[i] + palavra2[i]

            if(of == True): #Se houver overflow
                estado = estado + 1 #Estado é acrescentado um bit, o "vai um"
                of = False

            if(estado == 0):
                soma_1e2.insert(0, 0) #Se a soma das palavras é de 0+0, insere 0
                
            if(estado == 1):
                soma_1e2.insert(0, 1)  #Se a soma é de 0+1, insere 1

            if(estado == 2):
                soma_1e2.insert(0, 0) #Se a soma é de 1+1, insere 0 e vai para o overflow
                of = True

            if(estado == 3):
                soma_1e2.insert(0, 1) #Se a soma é 1+1+1 devido ao overflow anterior, insere um e overflow = true
                of = True 

            if( i == 0 and of == True): #Em caso de overflow, é chamada a função para somar com o overflow
                soma_1e2 = soma_of(soma_1e2)
                of = False

        
        soma_Re3 = []
        of = False
        for i in range( len(palavra1)-1, -1, -1): #O mesmo é feito para somar a 3a palavra
            estado = soma_1e2[i] + palavra3[i]

            if(of == True):
                estado = estado + 1
                of = False

            if(estado == 0):
                soma_Re3.insert(0, 0)
                
            if(estado == 1):
                soma_Re3.insert(0, 1)

            if(estado == 2):
                soma_Re3.insert(0, 0)
                of = True

            if(estado == 3):
                soma_Re3.insert(0, 1)
                of = True 

            if( i == 0 and of == True):
                soma_Re3 = soma_of(soma_Re3)
                of = False
 

        soma_ReEDC = []
        of = False
        for i in range( len(palavra1)-1, -1, -1): #Por fim, é somada a 3a palavra ao EDC, a fim de verificar se 
            estado = soma_Re3[i] + EDC[i] #A mensagem foi transmitida corretamente

            if(of == True):
                estado = estado + 1
                of = False

            if(estado == 0):
                soma_ReEDC.insert(0, 0)
                
            if(estado == 1):
                soma_ReEDC.insert(0, 1)

            if(estado == 2):
                soma_ReEDC.insert(0, 0)
                of = True

            if(estado == 3):
                soma_ReEDC.insert(0, 1)
                of = True 

            if( i == 0 and of == True):
                soma_ReEDC = soma_of(soma_ReEDC)
                of = False
        
        print(soma_ReEDC)

        if(soma_ReEDC == [1,1,1,1,1,1,1]): #Se o resultado da soma do EDC + soma das palavras transmitidas for todo 1
            l_check['text'] = "ENVIO CORRETO!" #A mensagem está correta
        else:
            l_check['text'] = "ENVIO INCORRETO!" #Caso haja pelo menos um dígito 0, a mensagem contém erros

        


#Interface gráfica

    window = tk.Tk()
    window.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12], minsize=20, weight=1)
    window.columnconfigure([0, 1, 2, 3], minsize=20, weight=1)
    window.title("CheckSum")
    window.geometry("500x500")

    l_palavra1 = tk.Label(master=window, text=' Palavra 1:')
    l_palavra1.grid(row=1,column=1)
    i_palavra1 = tk.Entry(master=window, width=60)
    i_palavra1.grid(row=1, column=2)

    l_palavra2 = tk.Label(master=window, text=' Palavra 2:')
    l_palavra2.grid(row=2,column=1)
    i_palavra2 = tk.Entry(master=window, width=60)
    i_palavra2.grid(row=2, column=2)

    l_palavra3 = tk.Label(master=window, text=' Palavra 3:')
    l_palavra3.grid(row=3,column=1)
    i_palavra3 = tk.Entry(master=window, width=60)
    i_palavra3.grid(row=3, column=2)

    b_gera_checkSum = tk.Button(master=window, text="Fazer checksum", width=60 , command=calcula_checkSum, bg="SteelBlue1")
    b_gera_checkSum.grid(row=4,column=1)

    l_edc = tk.Label(master=window, text= "EDC:")
    l_edc.grid(row=5, column=1)

    l_result_edc = tk.Label(master=window, text="")
    l_result_edc.grid(row=5, column=2)

    b_transmite = tk.Button(master=window, text="Transmite", command=Transmite, width=60, bg="red")
    b_transmite.grid(row=6,column=1)

    l_palavra_errada1 = tk.Label(master=window, text="")
    l_palavra_errada1.grid(row=7, column=1)
    l_palavra_errada2 = tk.Label(master=window, text="")
    l_palavra_errada2.grid(row=8, column=1)
    l_palavra_errada3 = tk.Label(master=window, text="")
    l_palavra_errada3.grid(row=9, column=1)

    b_check = tk.Button(master=window, text="Checar por erros", command=checka, width=60, bg="green")
    b_check.grid(row=10,column=1)

    l_check = tk.Label(master=window, text="")
    l_check.grid(row=11,column=1)

    l_tamanho = tk.Label(master=window, text="")
    l_tamanho.grid(row=12,column=1)

    window.mainloop()