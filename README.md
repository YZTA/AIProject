# Takım Numarası
### 103
## Takım Üyeleri
* Melih Can Şengün / Scrum Master
* Durmuş Ali Taner / Product Owner
* Çağla Nur Sorkun
* Ali Demirci
* Rabia Yolcu
# Ürün İle İlgili Bilgiler
## Ürünün İsmi
 * Ders Kitapları Yorumları Duygu Analiz (Pozitif/Negatif) Sistemi
## Product Backlog URL
* https://miro.com/app/board/uXjVIgi0pus=/?share_link_id=894717835749
 ![image](https://github.com/AliDmrcIo/AIProject/blob/main/1.sprint.png?raw=true)
## Ürün Açıklaması
* Bu proje, üniversite derslerinde kullanılan kitaplara yapılan yorumları analiz ederek, bu yorumların pozitif mi yoksa negatif mi olduğunu belirleyen yapay zeka destekli bir web sistemi geliştirmeyi hedeflemektedir.
Kullanıcılar sistem üzerinden kitaplar hakkında yorum okuyabilir, yorumlara göre fikir edinebilir ve isterlerse kendi yorumlarını da ekleyebilir.
Yapay zeka, yorumları duygu yönünden sınıflandırarak kitaplar hakkında daha objektif bir genel görüş sunar.
## Ürün Özellikleri
- Yorum arama: Kitap adına göre yorum arama
- Duygu analizi: Pozitif / negatif yorum ayrımı yapma
- Veri görselleştirme: Yorumların dağılımı ve duygu skoru
- Yorum ekleme: Kullanıcıların yeni yorum ekleyebilmesi
- Veri temizleme: Model için yorumların işlenmiş versiyonları
- Web arayüzü: Kitap listesi, yorum detayları, analiz sonuçları

________________________________________


# Sprint 1
## Ürün Durumu:
* UI kısmına 2. sprintte başlamaya karar verildiğinden dolayı web sitesi için ürün görseli bulunmamakta. Bu nedenle, aşağıya backend kısmındaki ilerlememizi gösteren birkaç fast api görseli ve terminal çıktıları eklenmiştir. 2.sprintte UI tasarımlarımızı göreceksiniz.
![image](https://github.com/AliDmrcIo/AIProject/blob/main/fastapi.jpeg?raw=true)
![image](https://github.com/AliDmrcIo/AIProject/blob/main/fastapi2.jpeg?raw=true=)
![image](https://github.com/AliDmrcIo/AIProject/blob/main/%C3%A7%C4%B1kt%C4%B11.jpeg?raw=true)
![image](https://github.com/AliDmrcIo/AIProject/blob/main/%C3%A7%C4%B1kt%C4%B12.jpeg?raw=true)
- **Sprint içinde tamamlanması tahmin edilen puan**: 70 Puan
- **Puan tamamlama mantığı**: Toplamda proje boyunca tamamlanması gereken 300 puanlık backlog bulunmaktadır. 3 sprint'e bölündüğünde ilk sprint'in yarısı fikir üretme ve araştırmaya ayrıldığından ilk sprint puanı 70 olarak kararlaştırılmıştır.
- **Daily Scrum**: Daily Scrum toplantı notları Trello üzerindeki ''Daily Scrum Meeting Notes'' bölümünden ulaşabilirsiniz. Toplantılar Google meets üzerinden gerçekleştirilmiştir.
- https://trello.com/invite/b/686513bcb351ad746fd6d6d6/ATTI97db9bd0468b087cddff5c9487e42ab6388E9A69/team103-1st-sprint
 ![image](https://github.com/AliDmrcIo/AIProject/blob/main/WhatsApp%20Image%202025-07-09%20at%2010.37.47.jpeg?raw=true)
 ![image](https://github.com/AliDmrcIo/AIProject/blob/main/WhatsApp%20Image%202025-07-09%20at%2010.37.48.jpeg?raw=true)
- **Sprint board update**: Sprint board screenshotları: 
![image](https://github.com/AliDmrcIo/AIProject/blob/1e4bcf1c18cdb2e1a55a546df264506aee7ffff5/1st.sprint.ss.jpg)
- **Sprint Review**:
*Tüm ekip toplantılara aktif bir şekilde katıldı.
*Proje ihtiyaçları başarıyla analiz edildi.
*Kullanıcı senaryoları çıkarıldı ve dökümante edildi.
*CV ve ilan verileri toplandı ancak veri araştırması devam edecek.
*Teknik mimari taslağı oluşturulamadı ve 2. sprinte ertelendi.
*Önümüzdeki sprintin planlanması yapılmaya başlandı.
- **Sprint Retrospektif**:
* Bu sprintte iş ve okul sebeplerinden görev alamayan arkadaşlarımıza ikinci sprintte görev tanımlamaları yapılması kararı alındı.
* Backend bölümü için daha fazla zaman ayırmaya karar verildi.
* İlk sprintte sprint hızımız yavaş kaldı, bunun kritiği yapıldı ve tamamlanması gerekenler 2. sprinte ertelendi.
* Önümüzdeki sprintin ortalama puanı 150 olarak belirlendi, sprint hızına göre bu puan arttırılabilir.
* UX UI tarafında çalışmalara ve web sayfası tasarımına başlanılacak.
* Eksik ve yavaş kaldığımız taraflarımız tarşıldı önümüzdeki sprint için önlemnler ve iyileştirmeler yapma kararı aldık.
* En güçlü yanlarımızdan biri olan ekip içi iletişim için tüm takım tebrik edildi.
- **1.Sprint Notu**: 
Genel olarak ilk haftayı ürün bulma ve araştırma olarak geçirdik tüm ekip arkadaşlarım toplantılara eksiksiz katıldı.
Ürün fikrini de genel bir oylama yaparak ve tartışarak kararlaştırdık ancak bazı teknik noktalar konusunda kararsız olduğumuzdan bu proje fikriyle devam edip etmeyeceğimizin kararı 2. sprintin başına ertelendi.
----------------------------------------------------------------------------
# Sprint 2
## Ürün Durumu:
* Bu sprintte ürün fikri netleşti ve yapay zeka destekli kitap yorum analizi sistemine odaklanıldı. Backend tarafında veri toplama ve ön işleme süreçleri başladı. UI kısmında ise ilk taslaklar oluşturuldu. Aşağıya hem backend’e dair çıktılar hem de UI taslaklarımızın ekran görüntüleri eklenmiştir.
![image](https://github.com/AliDmrcIo/AIProject/blob/main/fastapi.jpeg?raw=true)
- **Sprint içinde tamamlanması tahmin edilen puan**: 100 Puan
- **Puan tamamlama mantığı**:  Projenin toplam puanı 300 olarak belirlenmiştir. İlk sprintte fikir üretme ve araştırma yapıldığından dolayı daha az puan hedeflenmişti. Bu sprintte ürün fikri değişti ve teknik mimarisi oluşturulmaya başlandığı ve arayüz kısmına da geçildiği için 100 puan hedefi belirlenmiştir.
- **Daily Scrum**: Daily Scrum toplantı notları Trello üzerindeki ''Daily Scrum Meeting Notes'' bölümünden ulaşabilirsiniz. Toplantılar Google meets üzerinden gerçekleştirilmiştir.
- https://trello.com/b/Eje6mb0v/team103-2nd-sprint
 ![image](https://github.com/AliDmrcIo/AIProject/blob/main/WhatsApp%20Image%202025-07-09%20at%2010.37.47.jpeg?raw=true)
- **Sprint board update**: Sprint board screenshotları: 
![image](https://github.com/AliDmrcIo/AIProject/blob/1e4bcf1c18cdb2e1a55a546df264506aee7ffff5/1st.sprint.ss.jpg)
- **Sprint Review**:
* Ürün fikri tamamen netleştirildi.
* Kullanıcı senaryoları bu fikre göre güncellendi.
* Kitaplara yapılan yorumlar üzerinden duygu analizi yapacak sistemin veri seti araştırması başlatıldı.
* İlk yapay zeka modeli geliştirildi ve örnek analizler yapıldı.
* Backend servisleri Flask ile hazırlandı.
* UI tasarımlarına başlandı ve ana sayfa + kitap detay sayfası planlandı.
* Görev dağılımı netleştirildi ve puan bazlı ilerleme takibi yapılmaya başlandı.
- **Sprint Retrospektif**:
* İlk sprintte görev alamayan arkadaşlarımıza ikinci sprintte görev tanımlamaları yapıldı.
* UI UX tasarım bölümü için daha fazla zaman ayırmaya karar verildi.
* İlk ve ikinci sprintte sprint hızımız yavaş kaldı, bunun kritiği yapıldı ve tamamlanması gerekenler 3. sprinte ertelendi.
* Önümüzdeki sprintin ortalama puanı 150 olarak belirlendi, sprint hızına göre bu puan arttırılabilir.
- **2.Sprint Notu**: 
Bu sprintte artık ürün fikrimiz netleşti ve ekip olarak teknik geliştirmelere odaklanmaya başladık. Tüm ekip arkadaşlarım görevlerini zamanında teslim etmeye özen gösterdi. Backend tarafında ilk modeli geliştirip test ettik. UI tasarımı için temel çizimler yapıldı ve kullanıcı senaryolarına göre sayfa planlaması yapıldı. Üçüncü yani son sprintte ürünü tamamlamaya odaklanacağız.
----------------------------------------------------------------------------

