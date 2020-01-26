import sqlite3

try:

    # Veritabanı açma
    conn = sqlite3.connect('library.db')
 
    # Tablo oluşturma
    conn.execute('''CREATE TABLE `yazar` (
        `yazarNo`  INTEGER,
        `ad`   TEXT,
        PRIMARY KEY(`yazarNo`)
            )''')
 
    conn.execute('''CREATE TABLE `kitap` (
        `kitapNo`  INTEGER,
        `ad`   TEXT,
        `miktar`  TEXT,
        `yazar` INTEGER,
        PRIMARY KEY(`kitapNo`)
            )''')
 

        
    # Veritabanına yazma
    conn.commit()
 
    # Veritabanını kapatma
    conn.close()

    print("DB Olusturuldu")
        
except Exception as e:
    print(f"DB Olusturulmadı, Hata: {e}")

#yazar girişlerinin yapılması için fonksiyon
def yazarGiris():
    yazar_ad=input("Yazar adı girin: ")
    # bağlantıyı aç
    with sqlite3.connect("library.db") as conn:
        cur=conn.cursor()
        try:
            #kayıt et
            cur.execute('''INSERT INTO yazar (ad) VALUES(?)''',[yazar_ad])
            conn.commit()
            print("Yazar eklendi.")
        except Exception as e:
            print(e)

def kitapGiris():
    kitap_ad=input("Kitap adı girin: ")
    stok_adedi=input("Stok adedi girin: ")
    with sqlite3.connect("library.db") as conn:
        cur=conn.cursor()
        try:
            #yazar tablosundan yazarları alır
            cur.execute('''SELECT * FROM yazar ''')
            data=cur.fetchall()
        except Exception as e:
            print(e)
    print("yazar seçinmi yapın: ")
    #yazar seçimi için yazarları listeler
    for i in range(len(data)):
        print(f"{data[i][0]}:{data[i][1]}")
    yazarno=int(input())

    with sqlite3.connect("library.db") as conn:
        cur=conn.cursor()
        try:
            #kitap eklemek için sql
            cur.execute('''INSERT INTO kitap (ad,miktar,yazar) VALUES(?,?,?)''',[kitap_ad,stok_adedi,yazarno])
            conn.commit()
            print("Kitap eklendi.")
        except Exception as e:
            print(e)

def arama():
    aranacak = input("Aramak Istenilen: ").lower()

    with sqlite3.connect("library.db") as conn:
        cur = conn.cursor()
        try:
            #aranacak kitap veya yazarı arar
            cur.execute("""select k.kitapNo, k.ad, y.ad, k.miktar from yazar y, kitap k where y.yazarNo == k.yazar""")
            data_all=cur.fetchall()
        except Exception as e:
            print(e)

    print('{:^20} {:^20} {:^20} {:^20}'.format("No","Kitap Adı","Yazarı","Stok"))
    print('{:^20} {:^20} {:^20} {:^20}'.format("---------","---------","---------","---------"))

    for i in range(len(data_all)):
        if aranacak in data_all[i][1].lower() or aranacak in data_all[i][2].lower():
            print('{:^20} {:^20} {:^20} {:^20}'.format(data_all[i][0],data_all[i][1],data_all[i][2],data_all[i][3]))

def satis():
    print('{:^20} {:^20} {:^20} {:^20}'.format("No","Kitap Adı","Yazarı","Stok"))
    print('{:^20} {:^20} {:^20} {:^20}'.format("---------","---------","---------","---------"))

    with sqlite3.connect("library.db") as conn:
        cur = conn.cursor()
        try:
            #kitapları çeker ve listeleme yapar
            cur.execute("""SELECT * FROM kitap ORDER BY ad ASC""")
            data_k=cur.fetchall()
            #yazarları çeker    
            cur.execute("""SELECT * FROM yazar""")
            data_y=cur.fetchall()
        except Exception as e:
            print(e)
    #ekrana listeleme yapar
    for i in range(len(data_k)):
        for j in range(len(data_y)):
            if str(data_y[j][0]) == str(data_k[i][3]):
                print('{:^20} {:^20} {:^20} {:^20}'.format(data_k[i][0],data_k[i][1],data_y[j][1],data_k[i][2]))
        
    numara = input("Satılacak kitabın numarası: ")
    with sqlite3.connect("library.db") as conn:
        cur = conn.cursor()
        try:
            #kitapları çeker ve listeler
            cur.execute("""SELECT kitapNo,miktar FROM kitap""")
            kitaplar = cur.fetchall()
        except Exception as e:
            print(e)

    for i in range(len(kitaplar)):
        #eğer seçilen kitabın numarası i ye eşitse
        if int(numara) == int(kitaplar[i][0]):
            if int(kitaplar[i][1]) != 0:
                with sqlite3.connect("library.db") as conn:
                    cur = conn.cursor()
                    try:
                        #kitabı stoktan 1 azalt
                        cur.execute("""UPDATE kitap SET miktar = miktar-1 WHERE kitapNo = ?""", numara)
                        conn.commit()
                    except Exception as e:
                        print(e)

# switch case yapısı için dictionary kalıbı
def indirect(i):
    switcher={
            "y":yazarGiris,
            "k":kitapGiris,
            "a":arama,
            "s":satis
            }
    return switcher[i]()

while 1:
    print("\n")
    deger = input('{:^20} {:^20} {:^20} {:^20}'.format("[Y]azar Girişi","[K]itap Girişi","[A]rama","[S]atış")).lower()
    indirect(deger)