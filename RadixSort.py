#Cerco il max del vettore (O(n))

a=[13, 1, 5, 12, 45, 4, 2, 3, 2]
#a=[1,2,2,3,4,5,12,13,45]
b=[0]*len(a)
m = max(a)

def NumberToStringVect(A):
    B=[]
    for i in range(0, len(A)):
        B.append(str(A[i]))
    A=[]
    A=B.copy()
    del B
    return A


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
        C[int(A[j])] = C[int(A[j])]+1
    # Ho registrato il numero di copie che ho di ogni numero
    for i in range(1, max+1):
        C[i] = C[i]+C[i-1]
    #C[i] contiene tutti i numeri <= i
    for j in range(len(A)-1, -1, -1):
          B[int(C[int(A[j])])-1] = A[j]
          AI[int(C[int(A[j])])-1] = AIstr[j]
          C[int(A[j])] = C[int(A[j])] - 1
    print("Ordine parziale: ",AI)
    return AI



prova = [31274758, 43269326, 21047829, 78123209, 21979403]

#TODO domanda al prof: quindi uso sempre 24 bytes?
#converto a in binario



def RadixSort(A,p):

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
    print("Numeri da ordinare", B)
    #per ogni cifra ora creo le colonne parziali, k per r passi di dimensione p
    S=[]
    for k in range (0, r):
        S=[]
        D = [0] * len(A)  # array ordinato ad ogni passo reso dalla routine di counting sort
        B = NumberToStringVect(B)
        #prendo p cifre alla volta da ordinare
        for j in range(0, len(B)):
            S.append(B[j][(len(wordl)-p-k*p):(len(wordl)-k*p)])
        #print("s e' :", S)
        S = StringToNumberVect(S)
        B = StringToNumberVect(B)
        #S colonna da ordinare, B numeri da ordinare in toto, D colonna dei risultati
        OrdArray = CountingSortRadix(S, D, B, int(max(S)))
    print("Ordine finale: ",OrdArray)
RadixSort(prova, 2)
