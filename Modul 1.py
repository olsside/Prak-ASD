#1
def cetakSiku(x):
    for i in range(1,x+1):
        for y in range(1,i+1):
            print('*',end='')
        print()

#cetakSiku(5)
#2
def gambarlahPersegiEmpat(panjang, lebar):
    print("@"*lebar)
    panjang -= 2
    jarak = lebar -2
    while (panjang !=0):
        print("@"+(" "*jarak)+"@")
        panjang -= 1
    print("@"*lebar)
#gambarlahPersegiEmpat(4,5)
#3a
def jumlahHurufVokal(kata):
    vokal = "aiueo"
    panjang = len(kata)
    bykVokal = 0
    for i in kata:
        if i in vokal:
            bykVokal += 1
    print(panjang, bykVokal)
#jumlahHurufVokal("Surakarta")
#3b
def jumlahHurufKonsonan(kata):
    vokal = "aiueo"
    panjang = len(kata)
    bykKonso = 0
    for i in kata:
        if i not in vokal:
            bykKonso += 1
    print(panjang, bykKonso)
#jumlahHurufKonsonan("Surakarta")
#4
def rerata(angka):
    total = 0
    panjang = len(angka)
    for i in angka:
        total += i
    hasil = total / panjang
    return hasil
#print(rerata([3,5,6,2,7,4,8]))
#5
from math import sqrt as sq
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        hasil = ""
        for i in range(2,int(sq(n)+1)):
            if n%i == 0:
                hasil = False
                break
            else:
                hasil = True
        return hasil
#print(apakahPrima(25))
###6
def cetakPrima():
    for i in range(2,1001):
        for j in range(2,1001):
            if j>i:
                continue
            else:
                if i%j == 0:
                    if i!=j:
                        break
                    else:
                        print(i)
#cetakPrima()
###7
def faktorPrima(nilai):
    step = 1
    primaSmtr = []
    while(step<=nilai):
        step+=1
        for i in range(2,nilai+1):
            if nilai % i == 0:
                for j in range(2, i+1):
                    if i%j == 0:
                        if i == 2 or i==j:
                            nilai = nilai // i
                            primaSmtr.append(i)
                        else:
                            break
                break            
    print(primaSmtr)
###faktorPrima(120)
#8
def apakahTerkandung(a,b):
    if a in b:
        return True
    else:
        return False

#h = "do"
#k = "Indonesia tanah air beta"
#print(apakahTerkandung(h,k))
###9
def cetakPythonUMS():
    for i in range(1,101):
        if i%3 == 0 and i%5 == 0:
            print("Python UMS")
        elif i%3 == 0:
            print("Python")
        elif i%5 == 0:
            print("UMS")
        else:
            print(i)
#cetakPythonUMS()
#10
def selesaikanABC(a,b,c):
    from math import sqrt as akar
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if D<0:
        return 'Determinan negatif. Persamaan tidak mempunyai akar real'
    else:
        x1 = (-b + akar(D))/(2*a)
        x2 = (-b - akar(D))/(2*a)   
        hasil = (x1,x2)
        return hasil
###print(selesaikanABC(1,2,3))
#11
def apakahKabisat(tahun):
    if tahun%4 == 0:
        if tahun%100 == 0:
            if tahun%400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
###print(apakahKabisat(2021))
#12
def tebakAngka():
    import random
    angka = random.randint(1,100)
    percobaan = 1
    print("Permainan tebak angka")
    print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")
    while(percobaan<=7):
        tebak = input("Masukkan tebakan ke-"+str(percobaan)+":> ")
        if int(tebak) < angka:
            print("Itu terlalu kecil. Coba lagi.")
        elif int(tebak) > angka:
            print("Itu terlalu besar. Coba lagi.")
        else:
            print("Ya. Anda benar")
            break
        percobaan += 1
###tebakAngka()
#13
def katakan(n):
    ucapan = ['','Satu','Dua','Tiga','Empat','Lima',
              'Enam','Tujuh','Delapan','Sembilan','Sepuluh','Sebelas']
    if n <= 1000000000:
        hasil=''
        if n >= 0 and n <= 11:
            hasil = ucapan[n]
        elif n <20:
            hasil = ucapan[n-10] + ' Belas'
        #puluhhan (30,40m50 dst)
        elif n < 100:
            hasil = katakan(int(n/10)) + " Puluh " + ucapan[n%10]
        elif n < 200:
            hasil = 'Seratus ' + katakan(int(n-100))
        elif n < 1000:
            hasil = katakan(int(n/100)) + ' Ratus '+ katakan(int(n%100))
        elif n < 2000:
            hasil = 'Seribu '+katakan(n-1000)
        elif n < 1000000:
            hasil = katakan(int(n/1000)) + ' Ribu ' + katakan(int(n%1000))
        elif n < 1000000000:
            hasil = katakan(int(n/1000000)) + ' Juta '+ katakan(int(n%1000000))
        elif n == 1000000000:
            hasil = "Satu Milyar"
        
        return str(hasil)

    else:
        return "Jumlah tidak boleh lebih dari 1 milyar"
#print(katakan(x))
#x diganti angka dalam jutaan misal 2345678
#14
def formatRupiah(angka):
    angka = str(angka)
    sisa = len(angka)%3
    rupiah = "Rp "
    for i in range(len(angka)):
        rupiah += angka[i]
        if (i-sisa+4)%3==0 and i+1!=len(angka):
            rupiah += "."
    print(rupiah)
###formatRupiah(10000)
