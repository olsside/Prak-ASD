from MhsTIF import MhsTIF

c0 = MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = MhsTIF('Budi',51,'Sragen',230000)
c2 = MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = MhsTIF('Chandra',18,'Surakarta',235000)
c4 = MhsTIF('Eka',4,'Boyolali',230000)
c5 = MhsTIF('Fandi',31,'Salatiga',250000)
c6 = MhsTIF('Deni',13,'Klaten',245000)
c7 = MhsTIF('Galuh',5,'Wonogiri',245000)
c8 = MhsTIF('Janto',23,'Klaten',245000)
c9 = MhsTIF('Hasan',64,'Karanganyar',270000)
c10 = MhsTIF('Khalid',29,'Purwodadi',265000)

daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#1
listDaftar = []
def cari(data, target):
    for i in range(len(data)):
        if data[i].kotaTinggal == target :
            listDaftar.append(i)
    return listDaftar
#print(cari(daftar, "Klaten"))

#2
##def sakuKecil(data):
##    kecil = data[0]
##    for i in range(len(data)):
##        if data[i].uangSaku < kecil.uangSaku:
##            kecil = data[i]
##    k = str(kecil.nama)+" uang saku "+str(kecil.uangSaku)
##    return k
#print(sakuKecil(daftar))

#3
##def sakuKecil(data):
##    kecil = data[0]
##    listKecil = []
##    for i in range(len(data)):
##        for i in range(len(data)):
##            if data[i].uangSaku < kecil.uangSaku:
##                kecil = data[i]
##                listKecil.append(data[i])
##            elif data[i].uangSaku == kecil.uangSaku and data[i] not in listKecil and i!=0:
##                listKecil.append(data[i])
##    for i in listKecil:
##        print(str(i.nama)+" uang saku "+str(i.uangSaku))
##    return 
#print(sakuKecil(daftar))\

#4
def uangSaku(data, batas):
    total = []
    for i in data:
        if i.uangSaku < batas:
            total.append(i)
    for i in total:
        print(i)
    return 0
#print(uangSaku(daftar, 250000))

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(12)
head.next = Node(13)
head.next.next = Node(14)

#5
def cariItem(head, cari):
    x = head
    sekarang = 1
    while x != None:
        if x.data == cari:
            return "Item di simpul ke-"+str(sekarang)
        else:
            sekarang += 1
            x = x.next
    return "Item Tidak Ditemukan"

#print(cariItem(head, 13))

#kumpulan = [3,4,6,9,12,14,18,20]

#6
##def binSe(kumpulan, target):
##    low = 0
##    high = len(kumpulan)-1
##    while low <= high:
##        mid = (high + low)//2
##        if kumpulan[mid] == target:
##            return mid
##        elif target < kumpulan[mid]:
##            high = mid - 1
##        else:
##            low = mid +1
##    return false
#print(binSe(kumpulan,20))

kumpulan = [2,3,5,6,6,6,8,9,9,10,11,12,13,13,14]

#7
def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan)-1
    banyak = []
    while low <= high:
        mid = (high + low)//2
        if kumpulan[mid] == target:
            banyak.append(mid)
            if kumpulan[mid+1] == target:
                low = mid+1
            else:
                high = mid-1
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid +1
    banyak.sort()
    return banyak
#print(binSe(kumpulan,6))

#8
#pola nya titik tebakan tertinggi di akar 10 atau log 10
#hasil dari akar 10, di kalikan 3 (kesempatan menebak tiap satuan)
#hasil kali 3 ditambah 1 (untuk menenbak angkanya)
#Contoh:
#tebakan 1-1000
#1000 akar 10 = 3 (santuan, puluhan, ratusan) atau 10 log(1000) = 3
#3 kali 3 = 9 (tebakan tiap satuan)
#9 + 1 = 10(tebakan angkanya)
