lista=[]

def addelement():
    n=int(input("Quanti elementi vuoi aggiungere?"))
    for i in range(n):
        x=input()
        lista.append(x)
def show():
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")
def remove():
    show()
    valore=int(input("Quale elemento vuoi eliminare"))
    lista.pop(valore)
def count():
    print(len(lista))
def svuota():
    lista.clear()
def menu():
        print(f"inserisci 1 per aggiungere elementi")
        print(f"inserisci 2 per visualizzare gli elementi")
        print(f"inserisci 3 per togliere elementi")
        print(f"inserisci 4 per contare il numero degli elementi")
        print(f"inserisci 5 per svuotare la lista")
        print(f"inserisci 0 per fermare il programma")
while True:
    try:
        menu()
        d=int(input("cosa vuoi fare?"))
        if d == 1:
            addelement()
        elif d==2:
            show()
        elif d==3:
            remove()
        elif d==4:
            count()
        elif d==5:
            svuota()
        elif d==0:
            break
    except:
        print("riprova")
            

