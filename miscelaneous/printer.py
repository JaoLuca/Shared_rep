import random,time

#setar lista com caracters
charlist=['!','$','%','&','(',')','*','+','','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\'',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~','¡','¢','£','¤','¥','¦','§','¨','©','ª','«','¬','­','®','¯','°','±','²','³','´','µ','¶','·','¸','¹','º','»','¼','½','¾','¿','À','Á','Â','Ã','Ä','Å','Æ','Ç','È','É','Ê','Ë','Ì','Í','Î','Ï','Ð','Ñ','Ò','Ó','Ô','Õ','Ö','×','Ø','Ù','Ú','Û','Ü','Ý','Þ','ß','à','á','â','ã','ä','å','æ','ç','è','é','ê','ë','ì','í','î','ï','ð','ñ','ò','ó','ô','õ','ö','÷','ø','ù','ú','û','ü','ý','þ','ÿ']

# set looping method, time, imput (threading?), iterations (simplest)
def listcontruct(qtd):
    listing = []
    for i in range(qtd):
        r = int(random.random()*(len(charlist)))
        listing.append(charlist[r])

    return listing

def listcontructrandcharcteres():
    listing = []
    quantoschar = int(random.random()*500)
    for i in range(quantoschar):
        r = int(random.random()*(len(charlist)))
        listing.append(charlist[r])

    return listing

def listsend(qtdx, qtd,temp):
    for i in range(qtdx):
        if qtd:
            print (''.join(listcontruct(int(qtd))))   
        else:
            print(''.join(listcontructrandcharcteres()))   
                # print('.', end='')
                # time.sleep(0.01)
            # line = listcontructrandcharcteres()
            # for l in range(len(line)):
            #     print(line[l], end='')
            #     time.sleep(0.1)
        time.sleep(random.random()/temp)

try:
    qtd = input('Quantos caracteres: ')
    if not qtd:
        print('\nQuantidade aleatória de caracteres selecionado\n')
finally:
    qtdx = int(input("Quantas vezes: "))
    temp = input("Fração de segundo máxima: ")
    while temp=="":
        temp = input("Fração de segundo máxima: ")
    t0 = time.time()
    listsend(qtdx,qtd,int(temp))
    t1 = time.time()
    print('\nTempo decorrido: ' + str (t1-t0)+ " segundos\nQuantidade de listas: "+str(qtdx))

