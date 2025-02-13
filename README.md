# Akakce.com UI Test Otomasyonu

Bu proje, **Selenium WebDriver** ve **Python** kullanarak **Akakce.com** üzerinde UI testlerini gerçekleştirmek için geliştirilmiştir.  
Test senaryoları, bir kullanıcının web sitesi üzerinde gerçekleştirebileceği temel işlemleri otomatik olarak test etmeyi amaçlamaktadır.

---

## Test Senaryoları

1. **Kullanıcı Siteye Giriş Yapar**  
   - Kullanıcı **Akakce.com** adresine gider.  
2. **Kullanıcı Arama İşlemi Yapar**  
   - Örneğin, “iPhone” gibi popüler ve yorumu olan bir ürünü arar.  
3. **Kullanıcı Sonuç Listesinden Bir Ürün Seçer**  
   - Arama sonucunda çıkan ürün listesinden bir ürüne tıklar ve **"Ürüne Git"** seçeneğini kullanır.  
4. **Kullanıcı Ürünü Takip Listesine Ekler**  
   - Seçilen ürünü **takip listesine** ekler.  

---

## Kurulum ve Gereksinimler

### **1. Gerekli Araçlar**
- **Python 3.x** (Projenin çalıştırılabilmesi için)
- **pip** (Python paket yöneticisi)
- **Google Chrome veya Mozilla Firefox** (Testlerin çalıştırılması için)
- **ChromeDriver** (Selenium’un tarayıcıyı kontrol edebilmesi için)
- **Selenium WebDriver** (UI testleri için)

### **2. Projeyi Klonla**
GitHub üzerinden projeyi indir veya klonla:

```bash
git clone https://github.com/Hilal-Kocer/akakce_test_otomasyonu_UI.git
cd akakce_test_otomasyonu_UI
