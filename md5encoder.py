import hashlib

sifreleyici = hashlib.md5 #Noktadan sonraki kısmı md5 silin ve türevlerini yazın o şekilde de çalışacaktır.
metin = input("Lütfen hashlencek metin giriniz")
sifreleyici.update(metin.encode("utf-8"))
hash = sifreleyici.hexdigest()
print("Çıktı>>> %s" % hash )