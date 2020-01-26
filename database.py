import sqlite3

#ana kodumuzda çalıştırmak üzere fonksiyon
def run():
	try:
		# Veritabanı açma
		conn = sqlite3.connect('database.db')

		# Tablo oluşturma
		conn.execute('''CREATE TABLE `urunler` (
			`urunId`	INTEGER,
			`urunAdi`	TEXT,
			`kategori`	TEXT,
			`stok`	TEXT,
			`birimFiyati`	INTEGER,
			`satisFiyati` INTEGER,
			PRIMARY KEY(`urunId`)
				)''')

		conn.execute('''INSERT INTO "urunler" ("urunId", "urunAdi", "kategori", "stok", "birimFiyati", "satisFiyati") VALUES ('1', 'HP Omen', 'Bilgisayar', '500', '6000', '6300') ''')
		conn.execute('''INSERT INTO "urunler" ("urunId", "urunAdi", "kategori", "stok", "birimFiyati", "satisFiyati") VALUES ('2', 'Samsung S4', 'Telefon', '1500', '3500', '3700') ''')
		conn.execute('''INSERT INTO "urunler" ("urunId", "urunAdi", "kategori", "stok", "birimFiyati", "satisFiyati") VALUES ('3', 'Philips 54 ekran', 'Televizyon', '300', '8000', '8300') ''')
		conn.execute('''INSERT INTO "urunler" ("urunId", "urunAdi", "kategori", "stok", "birimFiyati", "satisFiyati") VALUES ('4', 'Huawei p30', 'Telefon', '60', '6300', '7000') ''')

		# Veritabanına yazma
		conn.commit()

		# Veritabanını kapatma
		conn.close()

		
		print("DB Olusturuldu")
		
	except Exception as e:
		print(f"DB Olusturulmadı, Hata: {e}")