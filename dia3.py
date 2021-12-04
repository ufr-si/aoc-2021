lista = []
with open("dia3.txt","r") as arquivo:
    for i in arquivo:
        lista.append(i[:-1])


gamma = 0
gamma_bin = "0"
epsilon_bin = "0"
epsilon = 0
uns = 0
zeros = 0
dec = len(lista[0])-1
for i in range(0,len(lista[0])):
    print("olhando : ",i)
    uns =0
    zeros = 0
    for numero in lista: 
        # pra cada numero na lista, conta
        if(numero[i] == "1"):
            uns = uns+1
        else:
            zeros = zeros+1
    print("uns: ",uns)
    print("zeros: ",zeros)
    if uns > zeros: 
        print("most common 1 ")
        gamma = gamma + (1*(2**dec))
        epsilon = epsilon + (0*(2**dec))
        gamma_bin = gamma_bin + "1"
        epsilon_bin = epsilon_bin+"0"
        dec = dec -1
    else:
        print("most common 0 ")
        epsilon = epsilon + (1*(2**dec))
        gamma = gamma +0*(2**dec)
        epsilon_bin = epsilon_bin+"1"
        gamma_bin = gamma_bin + "0"

        dec = dec -1

    print("gamma: ",gamma_bin)
    print("epsilon: ", epsilon_bin)

print("final: ")
print(gamma)
print(epsilon)
mult = gamma*epsilon
print(mult)
        

