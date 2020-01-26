#Uygulama başlayınca veritabanı dosyasından çağrılır ve veritabanı oluşturulur.
import database as Db
import sqlite3
Db.run()

# Veritabanına bağlanılır verilerin çekilmesine başlanır
with sqlite3.connect("database.db") as conn:
    cur = conn.cursor()
    # Vertabanında hata olması veya kapalı olması durumu için
    try:
        cur.execute("SELECT * FROM urunler")
        # gelen veriyi aldık
        data = cur.fetchall()
        cur.execute("SELECT name FROM pragma_table_info('urunler')")
        __temp__ = cur.fetchall()
        # Tablo keylerinin islenmesi.
        keys = []
        for i in range(len(__temp__)):
            # Duzgun bir formata sokmak icin string islemi.
            keys.append(str(__temp__[i])[2:-3])
    except Exception as e:
        print(e)


# Html dökumanı burada oluşturulur
html_file = open("html.html","w")


html_file.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Answer6</title>
</head>
<body>
<table>
    """) 
    
# Tablo başlıkları burada oluşturulur
html_file.write("<tr>")
for i in keys:
    html_file.write(f"<th>{i}</th>")
html_file.write("</tr>")

# Tablolara veri girişi burada yapılır
# Gelen dizinin boyutu kadar
for j in range(len(data)):
    html_file.write("<tr>")
    # her veriyi alır ve tablonun ilgili alanına yazar
    for i in range(len(data[j])):
        html_file.write(f"<td>{data[j][i]}</td>")
    html_file.write("</tr>")

html_file.write("""
</table>
</body>
</html>""")