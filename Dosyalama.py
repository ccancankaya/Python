import os
dosya=open("futbolcular.txt","w")
dosya.write("Fernando Muslera,Galatasaray\n")
dosya.write("Atiba Hutchinson,Beşiktaş\n")
dosya.write("Simon Kjaer,Fenerbahçe \n")
dosya.write("Ozan Tufan,Fenerbahçe \n")
dosya.write("Mariano,Galatasaray \n")
dosya.write("Taylan Antalyalı,Galatasaray \n")
dosya.write("Damagoj Vida,Beşiktaş \n")
dosya.write("Garry Rodriguez,Fenerbahçe \n")
dosya.write("Loris Karius,Beşiktaş \n")
dosya.write("Henry Onyekuru,Galatasaray \n")
dosya.write("Ömer Bayram,Galatasaray \n")
dosya.close()


with open("futbolcular.txt","r") as dosya:
    a=dosya.readlines()
    dosyaGs=open("gs.txt","w")
    dosyaFb=open("fb.txt","w")
    dosyaBjk=open("bjk.txt","w")

    for i in a:
        x=i.replace(" \n","").split(",")
        if str(x[1])=="Galatasaray":
            dosyaGs.write(x[0]+"\n"),
        if str(x[1])=="Fenerbahçe":
            dosyaFb.write(x[0]+"\n")
        elif str(x[1])=="Beşiktaş":
            dosyaBjk.write(x[0]+"\n")
    dosyaGs.close()
    dosyaFb.close()
    dosyaBjk.close()