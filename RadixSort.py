#Cerco il max del vettore (O(n))

a=[13, 1, 5, 12, 45, 4, 2, 3, 2]
#a=[1,2,2,3,4,5,12,13,45]
b=[0]*len(a)
m = max(a)

#CountingSort
def CountingSort(A, B, max):
    C=[]
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
def CountingSortRadix(A, B, AI, max):
    C=[]
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



prova = [31274758, 43269326, 21047829, 78123209, 21979403]

#TODO domanda al prof: quindi uso sempre 24 bytes?
#converto a in binario



def RadixSort(A,p):

    B=[]
    D = [] #array ordinato ad ogni passo reso dalla routine di counting sort
    C = [0]*len(A)
    for i in range(0, len(A)):
        B.append(str(A[i]))

    if len(B[1]) % p == 0:
      r = int(len(B[1])/p)

    else:
      # numero di volte che il ciclo verra ripetuto
      r = int(round((len(B[1])/p)+1))
    print("Totale passaggi:", r)
    print("Numeri da ordinare", B)
    #per ogni cifra ora creo le colonne parziali
    S=[]
    for k in range (0, r):
        S=[]
        for j in range(0, len(B)):
            S.append(B[j][(len(B[1])-p-k*p):(len(B[1])-k*p)])
            #TODO modificare e chiamare in modi corretto CountingSortRadix
            # CountingSortRadix()

        print("s e' :", S)
        #CountingSortRadix(S,B,D,max(S))

RadixSort(prova,2)