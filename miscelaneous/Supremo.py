#https://web.whatsapp.com/

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random
#Navegar até o Whats
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')

# Está configurado para mandar letra por letra

#time.sleep(20)
#driver.current_url
# Campo de mensagem e de busca 'copyable-text selectable-text'

def buscar_contato(contato):
    
    campo_de_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(1)
    campo_de_pesquisa.click()
    campo_de_pesquisa.send_keys(contato)
    time.sleep(1)
    campo_de_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(letra):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(1)
    for x in letra:
        l = x
        for y in l:
            campo_mensagem[1].send_keys(y)
            time.sleep(random.random()*1/30)
    
        campo_mensagem[1].send_keys(Keys.ENTER)

def enviar_várias(correio, quantas):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(1)
   
    aux = 0
    while aux<quantas :
        r = random.random()*len(correio)
        r=int(r//1)
        corre = correio[r]
        for x in corre:
            campo_mensagem[1].send_keys(x)
            time.sleep(random.random()*1/30)
        campo_mensagem[1].send_keys(Keys.ENTER)
        #time.sleep(random.random()*120) - Espera de até 2 min ente mensagens
        aux +=1


def desconectar (): #Needs an update, as the whatsweb disconnect menu has been updated.
    botao_conf = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div/span')
    botao_conf.click()
    time.sleep(2)
    botao_desconectar = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[3]/div/header/div[2]/div/span/div[3]/span/div[1]/ul/li[4]/div[1]')
    botao_desconectar.click()
    time.sleep(5)
    driver.close()

def definir_contatos():
    # Aqui você escreve exatamente o nome do contato pra quem vc quer mandar entre 'contato', vc pode mandar pra meas de uma conversa usando , e depois escrevendo a outra conversa entre 'grupo ou contato'
    contatos = []
    print('\n\nEscreva o nome de cada conversa exatamente como está em seu Whatsapp e aperte enter duas vezes após escolher o último contato (mesmo que eseja o único): \n')
    auxc = input()
    while auxc !='':
        contatos.append(auxc)
        auxc=input()
    return contatos
    
def definir_letra():
    letra = []
    print('\n\nCole abaixo a letra da música e digite ] para enviar: \n')
    aux = input()
    while aux !=']':
        letra.append(aux)
        aux=input()
    return letra

def muitas_mensagens(num, aux):
    if aux==0:
        todas_mensa = []
        mens = input('\nDigite as mensagens que quer mandar, elas serão escolhidas ao acaso para serem enviadas\nAperte enter duas vezes para começar a enviar.\n')
        while mens!='':
            todas_mensa.append(mens)
            mens = input()
    print('\nEntão Bora mandar, olha lá no Whats\n')
    buscar_contato(contato)
    # Colocar esse mecanismo dentro da função várias mensagens, para não ter que ficar chamnado ela diversas vezes    
    enviar_várias(todas_mensa, num)
    return todas_mensa
    

resp =''
caba = '/'
print('\n\nEscaneie o codigo QR para acessar seu WhatsApp\n\n')


while resp!= caba:
    
    contatos = definir_contatos()
    cont = 0
    while cont == 0:
        time.sleep(1)
        opcao = input('O que deseja fazer?\n\nEscreva "Várias" para mandar várias mensagens ou "Mensagens", para enviar a letra de uma música ou mensagens\n')
        if opcao == 'Mensagens':
            letra = definir_letra()
            cont = 1
        elif opcao == 'Várias':
            letra = []
            cont = 1
        else:
            print('\nPor favor digite exatamente Várias ou Mensagens\n')

    
    auxx=0
    con = 0
    for contato in contatos:
        if len(letra)>0:
            
            if con==0:
                print('\nEntão Bora mandar, olha lá no Whats\n')
                con+=1
            buscar_contato(contato)
            enviar_mensagem(letra)
        else:
            if auxx==0:
                n = int(input("\nQuantas mensagens quer mandar?\n"))
                todas = muitas_mensagens(n, auxx)
                auxx = 1
            else:
                buscar_contato(contato)
                enviar_várias(todas, n)
            
           
        
    
    resp = input('\n\nQUER CONTINUAR? \nDigite "/" sem as aspas paras encerrar a sessão, caso contrário aperte enter\n')
    if resp == caba:
        print('\n\nEntão foi isso familia\n')
        desconectar()
    





