import string

alfabeto = list(string.ascii_lowercase)

resultado = []

vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'w', 'z']

palavra = input("Informe uma palavra: ")
print(palavra)

for chave in range(0, 26):

        del resultado[:]
        constGuard = 0
        vogalGuard = 0
        for i in range(len(palavra)):
            for a in range(len(alfabeto)): 
                if palavra[i] == alfabeto[a]:
                    for c in range(len(consoantes)):
                        if alfabeto[a - chave] == consoantes[c]:
                            constGuard += 1
                            print(constGuard)
                    #for v in range(len(vogais)):
                        #if letra[g - chave] == vogais[v]:
                            #vogalGuard += 1
                            #print(vogalGuard)
                    resultado.append(alfabeto[a - chave])
        if constGuard < 25:
                print("--------", chave)
                StrResultado = "".join(resultado)
                print(StrResultado)
                          
                
              
 
