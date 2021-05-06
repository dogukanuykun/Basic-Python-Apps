import sqlite3
import time
con = sqlite3.connect("kutuphane.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (isim TEXT, yazar TEXT, Yayinevi TEXT, Sayfa_sayisi INT)")
    con.commit()
def veri_ekle(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("insert into kitaplik VALUES(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
def bilgiler():
    cursor.execute("SELECT * FROM kitaplik")
    data = cursor.fetchall()
    print("Bilgiler yükleniyor......")
    time.sleep(2)
    for i in data:
        print(i)
def isim_ve_yazar_bilgileri():
    cursor.execute("select isim,yazar from kitaplik")
    data = cursor.fetchall()
    print("bilgiler yükleniyor...")
    time.sleep(1)
    for i in data:
        print(i)
def isim_bilgiler(isim):
    cursor.execute("SELECT * from kitaplik where isim=?",(isim,))
    data = cursor.fetchall()
    for i in data:
        print(i)

isim_bilgiler("Sefiller")



con.close()

