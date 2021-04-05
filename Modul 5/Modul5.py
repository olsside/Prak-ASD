import ASDModul4 as a

daftar = a.daftar

#1
def swap(a,b,c):
    temp = a[b]
    a[b] = a[c]
    a[c] = temp

def cekNim(daftar):
    for i in daftar:
        print(i.nama,i.NIM,i.kotaTinggal)

def urutNim(daftar):
    for i in range(len(daftar)):
        for j in range(len(daftar)-1):
            if daftar[j].NIM > daftar[j+1].NIM:
                   swap(daftar,j,j+1)

##print("----Sebeleum-----")
##cekNim(daftar)
##urutNim(daftar)
##print("----Sesudah-----")
##cekNim(daftar)

#2
a = [13, 18, 25, 44, 66, 78, 89, 107]
b = [2, 4, 5, 10, 13, 18, 23, 29]

def urutC(a,b):
    c = a +b
    for i in range(len(c)):
        for j in range(len(c)-1):
            if c[j] > c[j+1]:
                swap(c,j,j+1)
    print(c)

##print(a)
##print(b)
##print("-----Digabung-----")
##urutC(a,b)

#3
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

#aw = detak();bubbleSort(u_bub);ak=detak();print("Bubble    : %g detik"%(ak-aw));
#aw = detak();selectionSort(u_sel);ak=detak();print("Selection : %g detik"%(ak-aw));
#aw = detak();insertionSort(u_ins);ak=detak();print("Insertion : %g detik"%(ak-aw));
