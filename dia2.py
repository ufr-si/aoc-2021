lista = []
with open("dia2.txt","r") as arquivo:
    for i in arquivo:
        lista.append(i[:-1])

print(lista)

# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.
def forward(n):
    global horizontal
    global vertical
    global aim
    horizontal = horizontal + n
    vertical = vertical+(aim*n)

# up X decreases your aim by X units.
def up(n):
    global vertical
    global aim
    #vertical = vertical - n
    aim = aim - n


# down X increases your aim by X units.
def down(n):
    global vertical
    global aim
    #vertical = vertical + n
    aim = aim + n


options = {"forward":forward,"up":up,"down":down}

horizontal = 0
vertical = 0 
aim = 0

for i in lista:
    print("i: ",i)    
    direcao = i.split(" ")[0]
    valor = int(i.split(" ")[1])
    options[direcao](valor)
    
    print("vertical: ",vertical)
    print("horizontal: ",horizontal)
    print("aim: ",aim )
    print("===")

res = horizontal*vertical
print(res)

