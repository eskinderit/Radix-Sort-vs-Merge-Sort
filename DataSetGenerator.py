import random
import math
import pickle
import sys


def random_boolean_num(bits):
    A = str()
    for j in range(0, bits):
        A = A+(str(random.getrandbits(1)))
    A = int(A)
    return A


def random_vect(B,bits):
    A=[]
    for i in range(B):
      A.append(random_boolean_num(bits))
    return A

def incr_vect(B):
    A=[]
    for i in range(B+1):
        A.append(i)
    return A

def decr_vect(B):
    A=[]
    for i in range(B,-1,-1):
        A.append(i)
    return A


def multiple_random_vect(MultipleNumberVect, step1, multi):
    numbervect1 = []
    for i in range(multi+1):
        numbervect1.append(i*step1)
    for j in range(len(numbervect1)):
        MultipleNumberVect.append(random_vect(numbervect1[j], 32))
    return MultipleNumberVect

def multiple_incr_vect(MultipleNumberVect, step1, multi):
    numbervect1 = []
    for i in range(multi+1):
        numbervect1.append(i*step1)
    for j in range(len(numbervect1)):
        MultipleNumberVect.append(incr_vect(numbervect1[j]))
    return MultipleNumberVect

def multiple_decr_vect(MultipleNumberVect, step1, multi):
    numbervect1 = []
    for i in range(multi+1):
        numbervect1.append(i*step1)
    for j in range(len(numbervect1)):
        MultipleNumberVect.append(decr_vect(numbervect1[j]))
    return MultipleNumberVect



# ATTENZIONE, NON ESEGUIRE QUESTO FILE: IL DATASET DI BASE VIENE MODIFICATO !!!
# Standard Data set to compare algs

##################### RANDOM BIG DATA SET #######################
SavedDataSet = []
multiple_random_vect(SavedDataSet, 5000, 20)
print(sys.getsizeof(SavedDataSet[1][1]))
pickle_out = open("randomBigDataset.pickle", "wb")
pickle.dump(SavedDataSet, pickle_out)
pickle_out.close()

##################### RANDOM SMALL DATA SET #######################
SavedDataSet = []
multiple_random_vect(SavedDataSet, 40, 5)
pickle_out = open("randomSmallDataset.pickle", "wb")
print(SavedDataSet)
pickle.dump(SavedDataSet, pickle_out)
pickle_out.close()


print("DATASET IS NOW REFRESHED")



