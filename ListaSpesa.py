lista=[]

def addelement():
    n=int(input("Quanti elementi vuoi aggiungere?"))
    for i in range(n):
        x=input()
        lista.append(x)
def show():
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")
addelement()
show()
