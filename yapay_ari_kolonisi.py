import math
from random import random
import numpy as np

#İTERASYON SÜRECİ
for dongu in range(0,durma_kriteri):
    
#İŞÇİ ARI SÜRECİ
#Bu safha işçi arıların besin kaynaklarına giderek mevcut besinlerden daha iyi daha uygun konumda olanları bulmaya çalıştığı safhadır.

    for ari in range(0,eb):
        
#Yeni besin kaynaklarının konumunun belirlennmesi 
#fi: besin kaynağı değişiminin rassal olarak yapılmasını sağlayan değer

    fi=-1+2*random()
    
    k=math.ceil(random()*eb)
    p=math.ceil(-1+(ts-1)*random())
    
    while ( k==ari):
        k(math.ceil(random())*eb)
    
#bu kısım tüm tasarım değişkenleri için tekrarlanmaktadır

    if(p==1):
        X1new=OPT[0][ari]+fi*(OPT[0][ari]-OPT[0][k])
        
    if(p==2):
        X2new=OPT[1][ari]4fi*(OPT[1][ari]-OPT[1][k])


 .....
 
#nektar_y: yeni kaynağın nektar miktarının değeri
    nektar_y[0][ari]=1/(1+OPT_Y[AF][ari])
    
#Bu algoritmada güncelleme,diğer algoritmalardan farklı olarak aşağıdaki gibi nektar miktarına göre gerçekleştirilmektadir. Bunun için;
#Yeni yiyecek kaynağının konumu/miktarı,her bir arının başlangıçta hafızasında tuttuğu kaynağındakinden daha iyiyse yeni kaynak hafzaya alınır.

    for ari in range(0,bk):
        if(nektar_y[0][ari]>nektar[0][ari]):
            OPT[0][ari]=OPT_Y[0][ari]
            OPT[1][ari]=OPT_Y[1][ari]
            


#Bu durumda başlangıç yiyecek konumunun güncellenmiş olma ihtimali göz önünde bulundurularak nektar miktarları tekrar hesaplanır.
    nektar[0][ari]=1/(1+OPT[AF][ari]) 
    
#Her bir arının bulduğu kaynağın iyileşmesine bağlı olarak KGL değerleri güncellenir.KAynak iyileştiriliyorsa bu parametre sıfırlanır aksi halde 
#değeri artırılarak kaynağın iyileştirilmemesine bağlı olarak tükenme durumu belirlenir.


    ip[0][ari]=0

else:
    ip[0][ari]=ip[0][ari]+1

    for ari in range(0,bk):
        besin_olasiligi[0][ari]=nektar[0][ari]/(sum(nektar))#nektar tekerleği yöntemi
        
#GÖZCİ ARI SAFHASI
#gözcü arılar işçi arılardan aldığı bilgilere göre kaynakların nektar miktarına göre belirlenen olasılık değerleri ile kaynak seçme işlemini gerçekleştirirler.

#besin kaynaklarının yeni konumunun besin olasılığı/kalitesiyle/ belirlenmesi

    for ari in range(0,ob):
        if (random()<besin_olasiliği[0][ari]): 
                
            k=math.ceil(random()*ob)
            p=math.ceil(-1+(ts-1)*random())
            
            
#fi: besin kakynağı değişiminin rassal olarak yapılmasını  sağlayan değer

        fi= -1+2*random()
        
        whilie(k==ari):
            k=math.ceil(random()*ob)
        
#Bu kısım tüm tasarım değişkenleri için tekrarlanmaktadır

        if(p==1):
            X1=OPT[0][ari]+fi*(OPT[0][ari]-OPT[0][k])
        
        if(p==2):
            X2=OPT[1][ari]+fi*(OPT[1][ari]-OPT[1][k])

......

    nektar_y[0][ari]=1/(1+OPT_Y[AF][ari])

#güncelleme 

#gözcü arıların belirlediği kaynakların konumu miktari işçi arılar tarafından bulunan kaynağındakinden daha iyiyse yeni kaynak hafızaya alınır.

    for ari in range(0,bk):
        if(nektar_y[0][ari]>nektar[0][ari]):
            OPT[0][ari]=OPT_Y[0][ari]
            OPT[1][ari]=OPT_Y[1][ari]
            ......
            
            
#bu durumda ,işçi arıların belirlendiği yiyecek konumunun güncellenmiş olma ihtimali göz önünde bulundurularak nektar miktarları tekrar hesaplanır.

    nektar[0][ari]=1/(1+OPT[AF][ari])
    ip[0][ari]=0
else:
    ip[0][ari]=ip[0][ari]+1

#İZCİ (KAŞİF) ARI SAFHASI
#bu aşamada konumu nektar miktar daha fazla iyileştirilmeyen kaynaklar KGL parametresine göre belirlenir ve kaynaklar terkedilerek yerine yeni (rastgele)
#besin kaynakların belirlenir.

    for ari im range(0,eb):
        if(ip[0][ari]>KGL):
            
            X1new=X1min+(X1maks-X1min)*random()
            X1new=X2m[İn+(X2maks-X2min)*random()
            ......
            
            
#nektarı tükenen kaynakların yenilenmesi sonucunda iyileştirilme parametreleri sıfırlanır ve böylece bir sonraki iterasyonda kullanılabilmesi sağlanır.

    ip[0][ari]=0
    
    #güncelleme
    
    for ari in range(0,bk):
        if(OPT[AF][ari]>OPT_Y[AF][ari]):
            OPT[0][ari]=OPT_Y[0][ari]
            OPT[1][ari]=OPT_Y[1][ari]
            ....
            
#iterasyon bitene kadar süreç içerisinde değerlendirilecek olan temel nektarı miktarı

    nektar[0][ari]=1/(1+OPT[AF][ari])
    
#iterasyon sonu 

#deger: tüm iterasyonlar sonucunda elde edilen en iyi çözümün amaç donksiyonu değeri
#sira: güncellenen OPT matrisinde bu çözümün yer aldığı vektör 
deger=min(OPT[AF][:])
sira=np.argmin(OPT[AF])
