matrik1 = [[x,x+1,x+2] for x in range(3)]
matrik2 = [[x,x+1,x+2] for x in range(3)]

#1a
def cekMatrik(x):
    lebar = len(x)
    for i in range(lebar):
        if len(x[i]) != lebar:
            print("Ukuran berbeda")
            return False
        return True

#print(cekMatrik(matrik1))

#1b
def cekUkuran(x):
    lebar = len(x)
    panjang = len(x[0])
    k = "Matrik ini memiliki ukuran "+str(panjang)+"x"+str(lebar)
    return k

#print(cekUkuran(matrik1))

#1c
def jumlahkanMatrik(x, y):
    if cekMatrik(x) != True:
        return False
    panjang = []
    lebar = []
    for i in range(0, len(x)):
        for j in range(0, len(x[0])):
            jumlah = x[i][j] + y[i][j]
            panjang.append(jumlah)
        lebar.append(panjang)
        panjang = []
    return lebar

#print(jumlahkanMatrik(matrik1, matrik2))

#1d
def hitungDeterminan(x):
    tambah = 0
    kurang = 0
    indeksA = 0
    indeksB = 0
    for h in range(0, 2):
        indeksA = 0
        indeksB = 0
        for i in range(0,len(x)):
            kali = 1
            for j in range(0, len(x[0])):
                kali *= x[indeksA][indeksB]
                if h == 0:
                    indeksA += 1
                    indeksB += 1
                    if indeksA >= len(x):
                        indeksA = 0
                    if indeksB >= len(x[0]):
                        indeksB = 0
                    tambah += kali
                else:
                    indeksA += 1
                    if j != len(x[0])-1:
                        indeksB -= 1
                    if indeksA >= len(x):
                        indeksA = 0
                    if indeksB < 0:
                        indeksB = len(x[0])-1
                    kurang += kali
            indeksA = 0
            if h == 0:
                indeksB += 1
    hasil = tambah - kurang
    return kurang

#hitungDeterminan(matrik1)

#2
#2a
def buatNol(x,y=None):
    if y == None:
        y = x
    matrik = [[0 for i in range(x)] for j in range(y)]
    return matrik

#2b
def buatIdentitas(x):
    matrik = [[1 if j==i else 0 for j in range(x)] for i in range(x)]
    return matrik


class Node(object):
    def __init__(self, data, next=None):
        self.data  = data
        self.next = next

#3
class List(object):
    def __init__(self):
        self.head = None
    def printList(self):
        head = self.head
        while(head != None):
            print('' + str(head.data)+"->", end = '')
            head = head.next
        print()
    def cari(self, yang_dicari):
        posisi = 1
        x = self.head
        while(True):
            if x.data != yang_dicari:
                x = x.next
                posisi += 1
            elif x == None:
                return "Data Tidak Ada"
                break
            else:
                return "Simpul ke-"+str(posisi)
                break
    def tambahDepan(self, head):
        tambah = Node(head)
        if self.head != None:
            tambah.next = self.head
        self.head = tambah
    def tambahAkhir(self, head):
        x = self.head
        tambah = Node(head)
        while(True):
            if self.head == None:
                self.head = tambah
            if x.next == None:
                x.next = tambah
                break
            else:
                x = x.next
    def tambah(self, head, posisi):
        sekarang = 0
        tambah = Node(head)
        x = self.head
        while x != None:
            if sekarang == posisi-2:
                tambah.next = x.next
                x.next = tambah
            elif posisi == 1:
                tambah.next = self.head
                self.head = tambah
                break
            elif x == None:
                break
            else:
                x = x.next
            sekarang +=1
    def hapus(self, posisi):
        sekarang =1
        x = self.head
        while x != None:
            if posisi ==1:
                x = x.next
                self.head = x
                break
            elif x.next == None and sekarang < posisi:
                break
            elif sekarang == posisi-1:
                x.next = x.next.next
            else:
                x = x.next
            sekarang +=1
            
#l = List()
#l.printList()
#l.tambahDepan(10)
#l.tambahAkhir(30)
#l.tambah(20, 2)
#l.printList()
#l.cari(20)
#l.hapus(2)
#l.printList()

#4
class Node2(object):
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class DoubleList(object):
    def __init__(self):
        self.head = None
    def cetakAll(self):
        head = self.head
        while head != None:
            print(head.data, end='->')
            if head.next != None:
                head = head.next
            else:
                break
        print()
        while self.head != None:
            print(head.data, end='->')
            if head.prev != None:
                head = head.prev
            else:
                break
        print()
    def tambahSimpulAwal(self, head):
        x = self.head
        tambah = Node2(head)
        if x == None:
            self.head = tambah
        else:
            x.prev = tambah
            tambah.next = x
            self.head = tambah
    def tambahSimpulAkhir(self, head):
        x = self.head
        tambah = Node2(head)
        while True:
            if x == None:
                self.head = tambah
                break
            elif x.next == None:
                x.next = tambah
                tambah.prev = x
                break
            else:
                x = x.next
#dl = DoubleList()
#dl.cetakAll()
#dl.tambahSimpulAwak(10)
#dl.tambahSimpulAkhir(20)
#dl.tambahSimpulAkhir(30)
#dl.cetakAll()
