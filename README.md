# Türkçe Kelime Türü Etiketleyici (POS Tagger)

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu proje, Türkçe metinler için geliştirilmiş, Koşullu Rastgele Alanlar (CRF) tabanlı bir Kelime Türü Etiketleyici (Part-of-Speech Tagger) sistemidir. Proje, bir metindeki her kelimenin dilbilgisel kategorisini (İsim, Fiil, Sıfat vb.) yüksek doğrulukla tespit eder ve sonuçları kullanıcı dostu bir grafiksel arayüz (GUI) ile sunar.

## Uygulama Arayüzü

![Uygulama Arayüzü](https://i.imgur.com/k6lP0W3.png)
*(Bu ekran görüntüsünü kendi en son ekran görüntünüz ile güncelleyebilirsiniz.)*

## 🚀 Özellikler

- **Yüksek Başarımlı Etiketleme:** Türkçe'nin morfolojik yapısına uygun, yüksek doğruluk oranı.
- **CRF Modeli:** Sıralı etiketleme problemlerinde kendini kanıtlamış Koşullu Rastgele Alanlar (CRF) modeli kullanılmıştır.
- **Profesyonel Veri Seti:** Model, Universal Dependencies (UD) projesinin [Turkish-IMST](https://github.com/UniversalDependencies/UD_Turkish-IMST) veri seti ile eğitilmiştir.
- **Kullanıcı Dostu Arayüz:** Tkinter ile geliştirilmiş, sonuçları renklendiren ve etiketleri Türkçeleştiren modern bir arayüze sahiptir.
- **Performans Göstergesi:** Modelin test verisi üzerindeki doğruluk oranını arayüzde gösterir.
- **Yardımcı Butonlar:** "Örnek Cümle" ve "Temizle" butonları ile kolay kullanım imkanı.
- **Komut Satırı Desteği:** Model eğitimi, değerlendirmesi ve etiketlemesi için tam fonksiyonel bir komut satırı arayüzü içerir.

## 🛠️ Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

**Gereksinimler:**
- [Python](https://www.python.org/downloads/) (3.9 veya üstü)
- [Git](https://git-scm.com/downloads/)

**Adımlar:**

1.  **Projeyi Klonlayın:**
    ```sh
    git clone [https://github.com/erdembaltaci/proje-repo-adi.git](https://github.com/erdembaltaci/proje-repo-adi.git)
    cd proje-repo-adi
    ```
    *(Not: `proje-repo-adi` kısmını kendi GitHub reponuzun adıyla güncelleyin.)*

2.  **Sanal Ortam Oluşturun ve Aktif Edin:**
    ```sh
    # Sanal ortamı oluştur
    python -m venv venv

    # Aktif et (Windows)
    venv\Scripts\activate

    # Aktif et (macOS/Linux)
    source venv/bin/activate
    ```

3.  **Gerekli Kütüphaneleri Yükleyin:**
    ```sh
    pip install -r requirements.txt
    ```

##  kullanım

Uygulamayı kullanmadan önce modelin eğitilmesi ve değerlendirilmesi gerekmektedir.

#### 1. Veri Setini Hazırlama (İlk Kurulumda Gerekli)

Proje, Universal Dependencies formatındaki (`.conllu`) veri setini kullanır. Bu veriyi projenin anlayacağı formata çevirmek için `veri_donusturucu.py` scriptini çalıştırın.

*(UD web sitesinden `tr_imst-ud-train.conllu` ve `tr_imst-ud-test.conllu` dosyalarını indirip projenin ana dizinine kopyaladığınızdan emin olun.)*

```sh
# Eğitim verisini dönüştür
python veri_donusturucu.py tr_imst-ud-train.conllu data/train/corpus.txt

# Test verisini dönüştür
python veri_donusturucu.py tr_imst-ud-test.conllu data/test/corpus.txt
```

#### 2. Modeli Eğitme ve Değerlendirme

Aşağıdaki komutları **sırayla** çalıştırarak modeli eğitin ve başarı skorunu hesaplayıp kaydedin.

```sh
# 1. Modeli eğit
python -m code.main --train

# 2. Modeli değerlendir (Bu adım, GUI'de gösterilecek skor dosyasını oluşturur)
python -m code.main --eval
```

#### 3. Grafiksel Arayüzü (GUI) Çalıştırma

Model eğitildikten ve değerlendirildikten sonra, kullanıcı arayüzünü başlatabilirsiniz:

```sh
python gui.py
```

#### 4. Komut Satırından Etiketleme (Opsiyonel)

Hızlı bir test için komut satırını da kullanabilirsiniz:
```sh
python -m code.main --tag "Bu cümle komut satırından etiketlendi."
```

## 👥 Proje Ekibi

- **Ali Erdem Baltacı** - 21360859011
- **Musa Adıgüzel** - 22360859328
- **Nazmi Cirim** - 21360859069
- **Siraç Gezgin** - 22360859058

## 📜 Lisans

Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) ile lisanslanmıştır.
