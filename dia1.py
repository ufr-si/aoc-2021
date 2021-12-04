aumentou = 0
lista = []
with open("input.txt","r") as arquivo:
    for i in arquivo:
        lista.append(i[:-1])
# A 
soma_janela_anterior = int(lista[0])+int(lista[1])+int(lista[2])
for i in range(3,len(lista)):
    anterior_2 = int(lista[i-2])
    anterior = int(lista[i-1])
    atual =  int(lista[i])
    soma_janela = atual +anterior+anterior_2

    if(soma_janela > soma_janela_anterior):

        aumentou = aumentou +1
    soma_janela_anterior = soma_janela
print(aumentou)