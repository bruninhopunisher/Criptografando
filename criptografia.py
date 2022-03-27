import string

alfabeto =list(string.ascii_lowercase)

palavra_crip = []

palavra = input('Digite sua palavra: ')
key = eval(input('Digite sua chave: '))

for p in range(len(palavra)):
    for a in range(len(alfabeto)):
        if (palavra[p] == alfabeto[a]):
            new_key = key + a
            while (new_key > 25):
                new_key = new_key - 26
            palavra_crip.append(alfabeto[new_key])
for i in range(len(palavra_crip)):
    str_palavra_crip = ''.join(palavra_crip)
print('\nPalavra criptografada: ')
print(palavra,'=', str_palavra_crip)

    









