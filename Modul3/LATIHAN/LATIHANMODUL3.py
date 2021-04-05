## Latihan 3.1
print("Latihan 3.1 Matrixs ebagai array duadimensi. Dibawah ini kita membuat ‘matrix’ 2×2 dan mengakses beberapa elemennya")
A = [ [2,3], [5,7] ]
print(A[0][1])
print(A[1][1])

## Latihan 3.2
print('Latihan3.2 Membuat matrix 3×3 berisi 0 semua.')
B = [ [ 0 for j in range(3)] for i in range(3) ]
print(B)

## Latihan 3.3

print('Membuat list kuadrat bilangandari0sampai6')
a = [x**2 for x in range(0,7)]
print(a)
print('Membuat list yang berisi tuple pasangan bilangan dan kuadratnya,dari 0 sampai 6')
b = [(x,x**2) for x in range(7)]
print(b)
#•Membuatlistkuadratbilangangenapantara0dan15>>>
c = [x**2 for x in range(15) if x%2==0]
print(c)
#•Membuatlistsepanjang5elemenyangberisibilangan3>>>
D = [3 for i in range(5)]
print(D)
#•Membuatlistsepanjangtigaelemenyangberisilistsepanjang3elemenangka0>>>
e = [[0 for j in range(3)]for i in range(3)]
print(e)
#•Membuatmatrixidentitas3×3
f = [[1 if j==i else 0 for j in range(3)]for i in range(3)]
print(f)
#•Membuatlistyangberisihurufvokalsuatustring>>>
d = ("YogyakartadanSurakarta.")
g = [x for x in d if x in "aiueoAIUEO"]
print(g)
##•Membuatlistbilanganprimaadari20sampai50>>>
##[xforxinrange(20,50)ifapakahPrima(x)][23,29,31,37,41,43,47]


class Node(object):
    """Sebuahsimpuldilinkedlist"""
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
a = Node(11)
b = Node(52)
c = Node(18)

a.next = b
b.next = c
print(a.data)
print(a.next.data)
print(a.next.next.data)
