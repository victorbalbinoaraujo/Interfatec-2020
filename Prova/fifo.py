processos = int(input())
aux = 0
tme = 0 
tmt = 0 

for i in range(processos):
    chegada = int(input())
    duracao = int(input())
    aux += duracao

    x = aux - (duracao + chegada)
    tme += x
    y = aux - chegada
    tmt += y

tme = tme / processos
tmt = tmt / processos       

print("TME: ", tme) 
print("TMT: ", tmt)    
