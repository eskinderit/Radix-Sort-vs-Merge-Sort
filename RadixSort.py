#Dati test

a=[13, 1, 5, 12, 45, 4, 2, 3, 2]
b=[0]*len(a)
m = max(a)

#Funzione per convertire numeri in stringhe
def NumberToStringVect(A):
    B=[]
    for i in range(0, len(A)):
        B.append(str(A[i]))
    A=[]
    A=B.copy()
    del B
    return A

#Funzione per convertire stringhe in numeri
def StringToNumberVect(A):
    B=[]
    for i in range(0, len(A)):
            B.append(int(A[i]))
    A = []
    A = B.copy()
    del B
    return A


#CountingSort
def CountingSort(A, B, max):
    C=[0]*(max+1)
    for j in range(0, len(A)):
        C[A[j]]=C[A[j]]+1
    # Ho registrato il numero di copie che ho di ogni numero
    for i in range(1, max+1):
        C[i]=C[i]+C[i-1]
    #C[i] contiene tutti i numeri <= i
    for j in range(len(A)-1, -1, -1):
          B[C[A[j]]-1] = A[j]
          C[A[j]] = C[A[j]] - 1
    return B

#CountingSort moddato per Radix, AI e' l'array intero
def CountingSortRadix(A, B, AIstr, max): #(S,D,B,max()) AIstr e' una matrice
    AI= [0]*(len(A))
    C = [0]*(max+1)
    for j in range(0, len(A)):
        C[(A[j])] = C[(A[j])]+1
    # Ho registrato il numero di copie che ho di ogni numero
    for i in range(1, max+1):
        C[i] = C[i]+C[i-1]
    #C[i] contiene tutti i numeri <= i
    for j in range(len(A)-1, -1, -1):
          B[(C[(A[j])])-1] = A[j]
          AI[(C[(A[j])])-1] = AIstr[j]
          C[(A[j])] = C[(A[j])] - 1
    print("Ordine parziale: ",AI,"\n")

    return AI



prova = [31274758, 31274757, 21047829, 78123209, 21979403]

#TODO domanda al prof:
# 1. Posso variare il passo, ma come lo studio analiticamnente senza i bit? devo considerasre che python usa 24 bit per intero
# 2. Devo studiare l'occupazione di memoria? e se si, come?
# 3. Vario il passo e faccio un confronto di quello o anche con altri algoritmi di ordinamento?
#TODO prima cifra non puo essere uno zero



def RadixSort(A,p):
    D = [0] * len(A)  # array ordinato ad ogni passo reso dalla routine di counting sort
    B=[]
    C = [0]*len(A)
    for i in range(0, len(A)):
        B.append(str(A[i]))
    wordl=B[1] #numero di cifre nel numero, si da per scontato sia un multiplo del passo
    if len(wordl) % p == 0:
      r = int(len(wordl)/p)

    else:
      # numero di volte che il ciclo verra ripetuto
      r = int(round((len(wordl)/p)+1))
    print("Totale passaggi:", r)
    print("Numeri da ordinare", B,"\n")
    #per ogni cifra ora creo le colonne parziali, k per r passi di dimensione p
    S=[]
    for k in range (0, r):
        S=[]

        B = NumberToStringVect(B)
        #prendo p cifre alla volta da ordinare
        for j in range(0, len(B)):
            S.append(B[j][(len(wordl)-p-k*p):(len(wordl)-k*p)])
        #print("s e' :", S)
        S = StringToNumberVect(S)
        B = StringToNumberVect(B)
        #S colonna da ordinare, B numeri da ordinare in toto, D colonna dei risultati
        B = CountingSortRadix(S, D, B, int(max(S)))
    print("Ordine finale: ",B)
RadixSort(prova, 2)

print(bin(5))