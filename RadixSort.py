import random
import math
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
import pickle

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

def TestRadix(File, step1, step2, step3, bits):
    RadixSortGraph1=[]
    RadixSortGraph2=[]
    RadixSortGraph3=[]
    pickle_in = open(File, "rb")
    Set = pickle.load(pickle_in)
    for j in range(1, len(Set)):
        RadixSortGraph1.append(RadixSort(Set[j], step1, bits))
        RadixSortGraph2.append(RadixSort(Set[j], step2, bits))
        RadixSortGraph3.append(RadixSort(Set[j], step3, bits))
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

############################# ESECUZIONE #######################


TestRadix("randomBigDataset.pickle", 1, 2, 4, 4)