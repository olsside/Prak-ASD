#LatihanModul2.py

#1
def ucapkanSalam():
    print("Assalamualaikum")
def kuadratkan(x):
    return x*x

buah = 'Mangga'
daftarBaju = ['batik','loreng','resmi berdasi']
jumlahBaju = len(daftarBaju)

#2
class Pesan(object):

    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumlah(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai',len(self.teks),'karakter.')
    def perbarui(self,stringBaru):
        self.teks = stringBaru
        
pesanA = Pesan('Aku suka kuliah ini')
pesanB = Pesan('Surakarta : the Spirit of Java')

##print(pesanA.cetakIni())
##print(pesanA.cetakJumlahKarakterKu())
##print(pesanB.cetakJumlahKarakterKu())
##print(pesanA.cetakPakaiHurufKapital())
##print(pesanB.cetakPakaiHurufKecil())
##print(pesanA.perbarui('Aku senang struktur data'))
##print(pesanA.cetakIni())

##
class sembarangKelas(object):
    def metodeSatu(self):
        pass
    def metodeSembilan(self, stringBaru):
        pass

obQ = sembarangKelas()
##print(obQ.metodeSatu())
##print(obQ.metodeSembilan('Aku suka mie ayam'))

#3
class Manusia(object):
    keadaan = 'lapar'
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self, s):
        print("Saya baru saja makan",s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self,n):
        return n*2

##p1 = Manusia('Fatimah')
##p1.ucapkanSalam()
##ak = Manusia('Abdul Karim')
##ak.ucapkanSalam()
##print(ak.keadaan)
##ak.makan('nasi goreng')
##print(ak.keadaan)
##ak.olahraga('renang')
##print(ak.keadaan)
##ak.makan('bakso')
##print(ak.keadaan)
##print(ak.mengalikanDenganDua(8))

#4
class Mahasiswa(Manusia):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal =kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM '+ str(self.NIM)\
            + '. Tinggal di '+ self.kotaTinggal \
            + '. Uang saku Rp '+ str(self.uangSaku)\
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        #Menutupi fungsi makan dari class Manusia
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = 'kenyang'

m1 = Mahasiswa('Jamil',234,'Surakarta',250000)
m2 = Mahasiswa('Andi',365,'Magelang',275000)
m3 = Mahasiswa('Sri',676,'Yogyakarta',240000)

##print(m1.ambilNama())
##print(m2.ambilNama())
##m3.ucapkanSalam()
##print(m3.keadaan)
##m3.makan('gado-gado')
##print(m3.keadaan)
##print(m3)

#5
#Beda File

#6
daftar = [m1,m2,m3]
##for i in daftar:
##    print(i.NIM)
##for i in daftar:
##    print(i)
##print(daftar[2].ambilNama())

#7
class kelasKosongan(object):
    pass

k = kelasKosongan()
k.x = 23
k.y = 47
##print(k.x+k.y)
##k.mystr = 'Indonesia'
##print(k.mystr)
