#kişiler listesini oluşturup içine 1 den 10001 e kadar sayı atıyor
persons=list(range(1,10001))
#kişilerin uzunluğu 1 den küçük olana kadar devam et
while len(persons)>1:
    #kişilerin içinde 1 den başlayarak dolanır
    for index,person in enumerate(persons):
        del persons[(index+1)%len(persons)]

print(persons)