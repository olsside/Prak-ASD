#1
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
#a
    def apakahTerkandung(self, kata):
        if str(kata) in self.teks:
            return True
        else:
            return False
#b
    def hitungKonsonan(self):
        vokal = 'aiueo'
        total = 0
        for i in self.teks:
            if i not in vokal and i != ' ':
                total += 1
        return total
#c
    def hitungVokal(self):
        vokal = 'aiueo'
        total = 0
        for i in self.teks:
            if i in vokal and i != ' ':
                total += 1
        return total
##p9 = Pesan('Indonesia adalah negeri yang indah')
##print(p9.apakahTerkandung('ege'))
##print(p9.apakahTerkandung('eka'))
##print('')
##p10 = Pesan('Surakarta')
##print(p10.hitungKonsonan())
##print('')
##print(p10.hitungVokal())

#Class Manusia
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
    
#2
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
#a
    def ambilKotaTinggal(self):
        return self.kotaTinggal
#b
    def perbaruiKotaTinggal(self, gantiKota):
        self.kotaTinggal = gantiKota
#c
    def ambilUangSaku(self):
        return self.uangSaku
    def tambahUangSaku(self, tambahUang):
        self.uangSaku += int(tambahUang)
#4
    listKuliah = []
    def ambilKuliah(self,Makul):
        self.listKuliah.append(Makul)
#5
    def hapusKuliah(self,Makul):
        if Makul in self.listKuliah:
            self.listKuliah.remove(Makul)
            print("Berhasil Menghapus Kuliah",Makul,"dari List")
        else:
            print("Mata Kuliah",Makul,"belum diambil")

##m9 = Mahasiswa('Tito',247,'Surabaya',270000)
##m9 = Mahasiswa('Tito',247,'Colomadu',200000)
##print(m9.ambilKotaTinggal())
##print('')
##m9.perbaruiKotaTinggal('Surakarta')
##print(m9.ambilKotaTinggal())
##print('')
##print(m9.ambilUangSaku())
##m9.tambahUangSaku(200000)
##print(m9.ambilUangSaku())

#3
##nama = input("Masukkan Nama : ")
##nim = int(input("Masukkan nim :(3 angka terkahir) "))
##alamat = input("Masukkan Alamat : ")
##uangSaku = int(input("Masukkan Uang Saku : "))
##print(Mahasiswa(nama,nim,alamat,uangSaku))
    
###Run no 4
##m234 = Mahasiswa('Tito',264,'Surabaya',270000)
##print(m234.listKuliah)
##m234.ambilKuliah('Matematika Diskrit')
##print(m234.listKuliah)
##m234.ambilKuliah('Agoritma dan Struktur Data')
##print(m234.listKuliah)
###Run no 5
##m234.hapusKuliah('Matematika Diskrit')
##print(m234.listKuliah)

#6
class SiswaSMA(Manusia):
    def __init__(self,nama,kelas,jurusan):
        self.nama = nama
        self.kelas = kelas
        self.jurusan = jurusan
    def __str__(self):
        kata = "Siswa bernama " + self.nama +\
               " dari Kelas " + str(self.kelas) +\
               " jurusan " + self.jurusan
        return str(kata)
    def perbaruiKelas(self,kelas):
        self.kelas = kelas
        print("Data berhasil diperbarui")
    def perbaruiJurusan(self,jurusan):
        self.jurusan = jurusan
        print("Data berhasil diperbarui")
        
##siswa1 = SiswaSMA("Tito",10,"IPS")
##print(siswa1)
##siswa1.perbaruiKelas(12)
##siswa1.perbaruiJurusan("IPA")
##print(siswa1)

#7
##NIM = Mahasiswa
##ambilKotaTInggal = Mahasiswa
##ambilNIM = Mahasiswa
##ambilNama = Mahasiswa
##ambilUangSaku = Mahasiswa
##katakanpy = MhsTIF
##kotaTinggal = Mahasiswa
##makan = Mahasiswa
##mengalikanDenganDua = Manusia
##nama = Mahasiswa
##olahraga = Manusia
##perbaruiKotaTinggal = Mahasiswa 
##tambahUangSaku = Mahasiswa
##uangSaku = Mahasiswa
##ucapkanSalam = Manusia
