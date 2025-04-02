lista=[]

def addelement():
    n=int(input("Quanti elementi vuoi aggiungere?"))
    for i in range(n):
        x=input()
        lista.append(x)

addelement()
