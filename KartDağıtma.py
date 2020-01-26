#rastgele dağıtmak için bu import edilmelidir
import random
#sayılar ve karakterler için ayrı diziler tanımlandı
karakterler = ["Karo","Maça","Sinek","Kupa"]
sayilar = [1,2,3,4,5,6,7,8,9,10,"Joker","Kız","Papaz"]
dagitim=[]

#dagitim dizisine karakterler ve sayılar girilir
for karakter in karakterler:
    for sayi in sayilar:
        dagitim.append(karakter + " " + str(sayi))

oyuncular={}

#herbir oyuncuya rastgele seçilen karakter veya sayı atanır 
for oyuncu in range(1,5):
    oyuncular["Oyuncu " + str(oyuncu)] = []
    for kart in range(1,13):
        kagit = dagitim.pop(dagitim.index(random.choice(dagitim)))
        oyuncular["Oyuncu "+ str(oyuncu)].append(kagit)

#ekrana sıralanır
for i in sorted(oyuncular):
    print ( "--------" + "\n" + i + "\n" + "--------")
    for j in oyuncular[i]:
        print (j)