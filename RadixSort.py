import random
import math
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
import pickle
import statistics



# rende un numero binario
def Binarize(array):
 for i in range(len(array)):
   array[i] = int(bin(array[i])[2:])
 return array

# genera vettore random di B numeri a bit bit
def random_vect(B,bit):
    A=[]
    for i in range(B):
      A.append(random.randint(0, 2**bit))
    return A

#  dimensione del vettore dei numeri da ordinare

def NumberToStringVectBin(A, expectedL):
    B=[]
    for i in range(0, len(A)):
        B.append(str(A[i]))
        while len(B[i]) != expectedL:
            B[i] = "0"+B[i]
    A=[]
    A=B.copy()
    del B
    return A


# Funzione per convertire numeri in stringhe
def NumberToStringVect(A):
    B=[]
    for i in range(0, len(A)):
        B.append(str(A[i]))
    A=[]
    A=B.copy()
    del B
    return A


# Funzione per convertire stringhe in numeri
def StringToNumberVect(A):
    B=[]
    for i in range(0, len(A)):
            if A[i]=="":
                B.append(0)
            else:
                B.append(int(A[i]))
    A = []
    A = B.copy()
    del B
    return A

# CountingSort
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

# CountingSort moddato per Radix, AI e' l'array intero
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
    #print("Ordine parziale: ",AI,"\n")
    return AI

# A vettore di numeri da ordinare, p passo, numberLen cifre per ogni numero
def RadixSort(A,p,numberLen):
    D = [0] * len(A)  # array ordinato ad ogni passo reso dalla routine di counting sort
    B=[]
    C = [0]*len(A)
    for i in range(0, len(A)):
        B.append(str(A[i]))
    if numberLen % p == 0:
      r = int(numberLen/p)

    else:
      # numero di volte che il ciclo verra ripetuto
      r = int(round((numberLen/p)+1))
    print("############# INIZIO RADIX ################## Totale passaggi:", r)
  ##  print("Numeri da ordinare", B,"\n")
    #per ogni cifra ora creo le colonne parziali, k per r passi di dimensione p
    S=[]
    start = timer()
    for k in range (0, r):
        S=[]
        B = NumberToStringVectBin(B, numberLen)
        #prendo p cifre alla volta da ordinare
        for j in range(0, len(B)):
            S.append(B[j][(numberLen-p-k*p):(numberLen-k*p)])
        #print("s e' :", S)
        S = StringToNumberVect(S)
        B = StringToNumberVect(B)
        #S colonna da ordinare, B numeri da ordinare in toto, D colonna dei risultati
        B = CountingSortRadix(S, D, B, int(max(S)))
    end = timer()
    print("Timer:",end-start)
    #print("Ordine finale: ",B)
    return end-start

def TestRadix(File, step1, step2, step3, bits, repeat):
    RadixSortGraph1=[]
    RadixSortGraph2=[]
    RadixSortGraph3=[]
    pickle_in = open(File, "rb")
    Set = pickle.load(pickle_in)
    Set1=Set.copy()
    Set2=Set.copy()
    for j in range(1, len(Set)):
        print("Test: ", File, "Passo: ", j, "/", len(Set))
        R1=[]
        R2=[]
        R3=[]
        for k in range(0, repeat):
            R1.append(RadixSort(Set[j], step1, bits))
            R2.append(RadixSort(Set1[j], step2, bits))
            R3.append(RadixSort(Set2[j], step3, bits))
        RadixSortGraph1.append(statistics.mean(R1))
        RadixSortGraph2.append(statistics.mean(R2))
        RadixSortGraph3.append(statistics.mean(R3))
    Set = []
    ElementsNum = []
    pickle_in = open(File, "rb")
    Set = pickle.load(pickle_in)
    for z in range(1, len(Set)):
        A = Set[z]
        ElementsNum.append(len(A))
    plt.plot(ElementsNum, RadixSortGraph1)
    plt.plot(ElementsNum, RadixSortGraph2)
    plt.plot(ElementsNum, RadixSortGraph3)
    plt.xlabel('Numero di elementi')
    plt.ylabel('Tempo di esecuzione')
    plt.title('Radix sort graph')
    plt.legend([step1, step2, step3])
    plt.show()

#   Merge Sort   #

def MergeSort(A, p, r):
    if p < r :
        q = (p+r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A, p, q, r)

#   Merge   #

def Merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[]
    R=[]
    for i in range (0,n1):
        L.append(A[p+i])
    for j in range (0,n2):
        R.append(A[q+j+1])
    L.append(math.inf)
    R.append(math.inf)
    i=0
    j=0
    for k in range (p,r +1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

# Merge sort with mask that returns timer #

def MergeSortMask(A, p, r):

    start = timer()
    MergeSort(A,p,r)
    end = timer()
    return end-start

def TestRadixVsMerge(File, step1, bits, repeat):
    RadixSortGraph1=[]
    MergeSortGraph=[]
    pickle_in = open(File, "rb")
    Set = pickle.load(pickle_in)
    Set1=Set.copy()
    for j in range(1, len(Set)):
        print("Test: ",File,"Passo: ",j,"/",len(Set))
        R1=[]
        M1=[]
        for k in range(0,repeat):
            R1.append(bitwiseRadixSort(Set[j], bits))
            M1.append(MergeSortMask(Set1[j], 0, len(Set1[j])-1))
        RadixSortGraph1.append(statistics.mean(R1))
        MergeSortGraph.append(statistics.mean(M1))
        print("tempo Radix: ", statistics.mean(R1))
        print("tempo Merge: ",statistics.mean(M1))
    Set = []
    ElementsNum = []
    pickle_in = open(File, "rb")
    Set = pickle.load(pickle_in)
    for z in range(1, len(Set)):
        A = Set[z]
        ElementsNum.append(len(A))
    plt.plot(ElementsNum, RadixSortGraph1)
    plt.plot(ElementsNum, MergeSortGraph)
    plt.xlabel('Numero di elementi')
    plt.ylabel('Tempo di esecuzione')
    plt.title('Radix sort graph')
    plt.legend(['Radix Sort', 'Merge Sort'])
    plt.show()

def bitwiseStableOrdering(A,i):
    B=[]
    C=[0, 0]
    mask = 2**i
    for j in range(len(A)):
        B.append(0)
        C[(A[j] & mask)//mask] += 1
    C[1]+= C[0]
    for j in range(len(A)-1, -1, -1):
        figure = (A[j] & mask)//mask
        C[figure] -= 1
        B[C[figure]] = A[j]
    return B


def bitwiseRadixSort(A,d):
    start = timer()
    B = A
    for i in range(d):
        B = bitwiseStableOrdering(B, i)
    end = timer()
    return end-start

############################# ESECUZIONE #######################

if __name__ == "__main__":
    #TestRadix("randomSmallDataset.pickle", 3, 4, 9, 32, 1)
    TestRadixVsMerge("randomBigDataset.pickle", 8, 8, 1) #file,step.bits,repeats


# TODO creare dataset da vari bit