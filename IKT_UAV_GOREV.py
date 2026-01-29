
#-------------VİDEO 3-------------
x=7
y="7"

print(type(x))
print(type(y))
#-------------VİDEO 5-------------
# Değişken İsim Çeşitleri

okulNo=380 #Camel Case
OkulNo=380 #Pascal Case
okul_no=380 #Snake Case
#-------------VİDEO 8-------------
import sys
boyut="asdasd"
print(sys.getsizeof(boyut)) #Ramde ne kadar bitlik yer kapladığını söyler.
#-------------VİDEO 9-------------
x=str(True) #Veri tipi bu şekilde değiştirilir.
y=range(7) #Girilen sayıya kadar dizi oluşturur. Sayı dahil değildir.
#-------------VİDEO 10------------
x=7
y=34587348578
z=-2535345

print("x: ",x,"\ny: ",y,"\nz: ",z) #Satır satır print'ten çıktı alma yöntemi.
#-------------VİDEO 11------------
#Random Modülü Fonksiyonları

import random as rnd 

rnd.seed(10)
print(rnd.random()) #Seed vererek rastgele sayı üretme algoritmasını açık bir şekilde 
                    #müdahale edebiliyoruz. Bu sayede tekrarlanabilir bir sonuç alabiliriz.

state=rnd.getstate()
print(rnd.random())

rnd.setstate(state)
print(rnd.random())

print(rnd.getrandbits(8)) #Girilen sayı kadar bit boyutunda rastgele sayı üretir.

print(rnd.randrange(1,10)) #Girilen aralık arasından rastgele sayı üretir. 
print(rnd.randint(1,10)) #Range'den farklı olarak ikinci sayı listeye dahildir.
#-------------VİDEO 12------------
listem=["kırmızı","beyaz","siyah"]
print(rnd.choice(listem)) #Girilen listeden rastgele bir elemanı alır.
print(rnd.choices(listem, weights=[1,10,1,], k=10)) #Weights elemanların ağırlığını, k ise kaç elemanlı olacağını belirler.
print(rnd.uniform(30,70)) #Girilen aralık arasından rastgele sayı üretir.
#-------------VİDEO 14------------
yazilar="IKT UAV" 
for yazi in yazilar:
    print(yazi) #Harf harf yazar. 

print("UAV" in yazilar) #Değer var mı yok mu söyler.
#-------------VİDEO 15------------
print(yazilar[0:4]) #Dilimleme yapar.
#-------------VİDEO 16------------
print(yazilar.upper) #Hepsini büyük yapar.
print(yazilar.lower) #Hepsini küçük yapar.
print(yazilar.replace("I","O")) #Verilen ifadeyi diğer ifade ile değiştirir.
#-------------VİDEO 18------------
isim="kemal"
yas="30"
yazili_not=3.4574857
text1="my name is {} im {} years old".format(isim,yas)
text2=f"my name is {isim} im {yas} years old" #f-string
text3=f"notum: {yazili_not:.3f}" #Ondalığa göre kesim yapar.
#-------------VİDEO 21------------
text4="Şükrü"
result4=text4.encode(encoding="ascii", errors="namereplace") #ASCII tablosunda olmayan karakterleri betimler.
print(result4)
#-------------VİDEO 22------------
print(yazilar.count("IKT")) #İçinde kaç adet olduğunu söyler.
#Tüm string metotları için https://www.w3schools.com/python/python_ref_string.asp
#-------------VİDEO 31------------
sayi1=7
sayi1&=5 # &= operatörü girilen iki sayının binary kodunu alır ve çarpar.
#-------------VİDEO 31------------
sayi2=16
sayi2>>=4 #2'nin 4. kuvvetine bölündüğündeki sonucu söyler.
#-------------VİDEO 36------------
#List Veri Türü

myList=["Fehmi",True,36,'a'] #veya 
myList=list(("Fehmi",True,36,'a')) #şeklinde tanımlanabilir.
print(myList[2:]) #2. indeksten sonrasına kadar alır.
#-------------VİDEO 47------------
#Örnek Bir For Yapısı
meyveler=["elma","armut","kiwi","karpuz"]
for meyve in meyveler:
    print(meyve,end=" ")
#-------------VİDEO 53------------
#Listenin Her Bir Elemanını For ile Yazdırma

for index in range(len(meyveler)):
    print(meyveler[index])

#Kısa Hali
[print(items) for items in meyveler]

new_list=[items for items in range(10)] #Satır Tasarrufu Sağlar
#-------------VİDEO 59------------
#Tuple Veri Türü
#Değiştirilemezdir. Sonradan bir oyunama mümkün değildir.

sayilar=(1,243,3454,656,34,123)
meyveler_tuple=tuple(meyveler)
(a,b,c,d)=meyveler_tuple #Paketleme
#-------------VİDEO 63------------
#Set Veri Türü
#Değiştirilemezdir. Sıralanmış değildir. Yinelenemez.

marka={"buzdağı","fuska","erikli","hamidiye"}
marka.add("hayat")
#-------------VİDEO 67------------
#Dictionary Veri Türü
#Değiştirilebilir. Sıralanmıştır. Yinelenemez.

araba={
    "marka":"opel",
    "model":"corsa",
    "electric":False,
    "renkler":["beyaz","kirmizi","mavi"],
    "yil":2007
    }
araba.pop("yil") #Değeri siler.

#Diğer bir oluşturma yöntemi:
insan=dict(boy=155,isim="mahmut",memleket="diyarbakır")
insan.keys #Anahtarları alır.
insan.values #Değerleri alır.
#-------------VİDEO 70------------
#Fonksiyonlar
def myFunc(name):
    print(name+" kardesime selamlar.")

myFunc("mahmut")
#-------------VİDEO 71------------
def Func2(**degiskenler):
    print("Soyadı şudur:"+degiskenler["lastname"])

Func2(lastname="Aktepe", firstname="Humeyra")

def Func3(degisken="default değer"):
    print("Değer"+ degisken)
Func3()

def Func4(degisken2):
    return degisken2*2
print(Func4(5))
#-------------VİDEO 87------------
#DateTime Modülü
import datetime
from datetime import datetime as dt 
from datetime import timedelta as td

print(dir(datetime)) #Bir kütüphanenin içindeki classları görüntülememizi sağlar.
date=dt.now() #veya .today()
print(date.hour)
print(date.second)
#-------------VİDEO 88------------
time=dt.now()
futuretime=time+td(days=7)
#-------------VİDEO 89------------
import time
baslangic=time.process_time()
for i in range(10000000000):
    pass
bitis=time.process_time()

print(bitis-baslangic)
#-------------VİDEO 97------------
class Sinif:
    def __init__(start):
        print("Nesne oluşturuldu.")

sinif=Sinif()
#-------------VİDEO 98------------
#Miras Alma İşlemi
class KucukSinif(Sinif):
    pass
#Eğer miras almak istediğimiz şeyler bir class'ın hepsi değilse almak istenilen
#metotları super().metotadi(parametreler) ile de kopyalayabiliriz.
#-------------VİDEO 104------------
#Class'lardaki metotların erişim seviyeleri şu şekilde belli olur:
#__metot__ Private
#_metot_   Protected
#metot     Public
#-------------VİDEO 107------------
#Abstract Class (Soyut Sınıf)
from abc import ABC,abstractmethod

class  Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

#Abstract Classı genel olarak yazılımcıları yönlendirmek içindir. Oluşturulacak olan 
#Child Class'lara metot ismi konusunda bir şablon gösterir.
#-------------VİDEO 110------------
#İçiçe Class'lar

class Car:
    pass

    def __init__(self,a,b,aa,bb):
        self.engine=Car.Engine(aa,bb)

    def show_details(self):
        print(self.engine.show_engine)

    class Engine:
        def __init__(self, a, b):
            self.deneme1=a
            self.deneme2=b
        def show_engine(self):
            return self.deneme1+self.deneme2
#-------------VİDEO 111------------
#Class Metodu

class Person:
    def __init__(self, age, name):
        self.age=age
        self.name=name

    @classmethod #Class'tan bir nesne oluşturmadan direkt olarak kullanmamızı sağlıyor.
    def birth_year(year,name):
        calculated_age=2026-year

        return Person(calculated_age,name)
    
    #instance method
    def display_info(self):
        print(f"{self.name}, {self.age} yaşındadır.")

p1=Person.birth_year(1990,"Hümeyra")
print(p1.display_info())
#-------------VİDEO 112------------
#Getter Setter ve Deleter

class Name:
    def __init__(self,name):
        self.name=name

    def get_name(self): #Getter Method
        return self.name
    
    def set_name(self,new_name): #Setter Method
        self.name=new_name

    def delete_name(self):
        self.name=None


def newMethod(self):
    print("New method added!")
class newClass:
    pass

newClass.newMethod=newMethod() #Dışardan method ekledik. 
#-------------VİDEO 118------------
#Try ve Except Kullanımı

try:
    print(time)
    
except NameError:
    print("Variable time is not defined.")
#-------------VİDEO 129------------
#JSON Kullanımı

