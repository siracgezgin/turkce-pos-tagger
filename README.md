<p align="center">
  <img src="https://i.imgur.com/your-logo-placeholder.png" alt="Proje Logosu" width="150"/>
</p>

<h1 align="center">Türkçe Kelime Türü Etiketleyici (POS Tagger)</h1>

<p align="center">
  Türkçe metinler için Koşullu Rastgele Alanlar (CRF) tabanlı, yüksek başarımlı ve kullanıcı dostu bir Kelime Türü Etiketleme (POS Tagging) sistemi.
  <br />
  <br />
  <a href="#-kullanım"><strong>Uygulamayı Keşfet »</strong></a>
  <br />
  <br />
  <a href="https://github.com/erdembaltaci/proje-repo-adi/issues">Hata Bildir</a>
  ·
  <a href="https://github.com/erdembaltaci/proje-repo-adi/issues">Özellik İste</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Framework-Tkinter-red?logo=tkinter" alt="Framework">
  <img src="https://img.shields.io/badge/Model-CRF-green" alt="Model">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

---

### İçindekiler

1.  [Proje Hakkında](#-proje-hakkında)
    * [Geliştirildiği Teknolojiler](#-geliştirildiği-teknolojiler)
2.  [Öne Çıkan Özellikler](#-öne-çıkan-özellikler)
3.  [Kurulum ve Başlangıç](#%EF%B8%8F-kurulum-ve-başlangıç)
4.  [Kullanım](#-kullanım)
    * [İş Akışı](#-i̇ş-akışı)
5.  [Proje Mimarisi](#-proje-mimarisi)
6.  [Lisans](#-lisans)
7.  [Proje Ekibi](#-proje-ekibi)
8.  [Teşekkür](#-teşekkür)

---

## 📖 Proje Hakkında

<p align="center">
  <img src="https://i.imgur.com/k6lP0W3.png" alt="Uygulama Ekran Görüntüsü" width="80%">
</p>

Bu proje, **Doğal Dil İşlemeye Giriş** dersi kapsamında geliştirilmiştir. Temel amacı, Türkçe gibi morfolojik açıdan zengin ve eklemeli dillerin getirdiği zorlukları aşarak, metin içerisindeki her bir kelimeyi dilbilgisel kategorisine (İsim, Fiil, Sıfat vb.) doğru bir şekilde atamaktır.

Sistem, istatistiksel bir sıralı etiketleme modeli olan **Koşullu Rastgele Alanlar (Conditional Random Fields - CRF)** algoritmasını temel alır. Bu model, kelimelerin sadece kendi özelliklerine değil, aynı zamanda çevrelerindeki kelimelerin bağlamına da bakarak karar verir. Bu sayede, "yüz" gibi çok anlamlı kelimelerin doğru etiketlenmesinde yüksek başarım göstermektedir.

Modelin eğitimi, **Universal Dependencies** projesinin kapsamlı **Turkish-IMST** veri seti kullanılarak gerçekleştirilmiştir. Son kullanıcı etkileşimi için Python'un standart kütüphanesi olan **Tkinter** ile geliştirilmiş, sonuçları renklendiren ve Türkçeleştiren modern ve kullanıcı dostu bir grafiksel arayüz (GUI) sunulmuştur.

### 💻 Geliştirildiği Teknolojiler

Bu projenin hayata geçirilmesinde kullanılan ana teknolojiler ve kütüphaneler:

* **Python:** Projenin ana programlama dili.
* **scikit-learn & sklearn-crfsuite:** CRF modelinin implementasyonu ve eğitimi için.
* **Tkinter:** Kullanıcı dostu masaüstü arayüzünün geliştirilmesi için.
* **Joblib:** Eğitilmiş modelin serileştirilmesi ve kaydedilmesi için.
* **JSON:** Model performans skorlarının saklanması için.

---

## ✨ Öne Çıkan Özellikler

* **🧠 Akıllı Modelleme:** Bağlamı anlayan CRF modeli sayesinde Türkçe'nin yapısal zorluklarına karşı yüksek doğruluk.
* **📊 Profesyonel Veri Seti:** Binlerce etiketli cümle içeren standart bir akademik veri seti (UD Turkish-IMST) ile eğitilmiştir.
* **🎨 Etkileşimli Arayüz:** Sonuçları etiket türüne göre renklendiren, Türkçeleştiren ve kullanımı kolaylaştıran butonlar içeren modern bir GUI.
* **📈 Performans Ölçümü:** Modelin test verisi üzerindeki doğruluk oranını (`Accuracy`) arayüzde net bir şekilde gösterir.
* **⚙️ Modüler ve Genişletilebilir Kod:** Proje, iyi organize edilmiş dosya yapısı sayesinde yeni özellikler eklemeye ve geliştirmeye müsaittir.
* **🖥️ Çift Arayüz Desteği:** Hem son kullanıcılar için grafiksel arayüz (GUI) hem de geliştiriciler için komut satırı arayüzü (CLI) sunar.

---

## ⚙️ Kurulum ve Başlangıç

Bu projeyi yerel makinenizde kurup çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### Gereksinimler
* [Python](https://www.python.org/downloads/) (Sürüm 3.9 veya üstü)
* [Git](https://git-scm.com/downloads/)

### Kurulum Adımları

1.  **GitHub Reposunu Klonlayın:**
    ```sh
    git clone [https://github.com/erdembaltaci/proje-repo-adi.git](https://github.com/erdembaltaci/proje-repo-adi.git)
    cd proje-repo-adi
    ```
    *(Not: `proje-repo-adi` kısmını kendi GitHub reponuzun adıyla güncelleyin.)*

2.  **Sanal Ortam (Virtual Environment) Oluşturun:**
    Bu, proje bağımlılıklarını sisteminizin geri kalanından izole etmek için en iyi yöntemdir.
    ```sh
    python -m venv venv
    ```

3.  **Sanal Ortamı Aktif Hale Getirin:**
    * Windows üzerinde:
        ```sh
        venv\Scripts\activate
        ```
    * macOS veya Linux üzerinde:
        ```sh
        source venv/bin/activate
        ```

4.  **Gerekli Kütüphaneleri Yükleyin:**
    `requirements.txt` dosyası, projenin ihtiyaç duyduğu tüm kütüphaneleri içerir.
    ```sh
    pip install -r requirements.txt
    ```
Kurulum tamamlandı! Artık projeyi kullanmaya hazırsınız.

---

## 🚀 Kullanım

Projenin tam potansiyelini kullanmak için aşağıdaki iş akışını takip etmeniz önerilir.

### 📋 İş Akışı

1.  **Veri Hazırlama (Sadece İlk Kurulumda):**
    Modeli eğitmek için standart CoNLL-U formatındaki veri setini projemizin formatına çevirmemiz gerekiyor. [UD Turkish-IMST](https://github.com/UniversalDependencies/UD_Turkish-IMST) reposundan `tr_imst-ud-train.conllu` ve `tr_imst-ud-test.conllu` dosyalarını indirip projenin ana dizinine kopyalayın. Ardından aşağıdaki komutları çalıştırın:
    ```sh
    # Eğitim verisini projemiz için hazırla
    python veri_donusturucu.py tr_imst-ud-train.conllu data/train/corpus.txt

    # Test verisini projemiz için hazırla
    python veri_donusturucu.py tr_imst-ud-test.conllu data/test/corpus.txt
    ```

2.  **Model Eğitimi:**
    `data/train` klasöründeki binlerce cümlelik veri setini kullanarak CRF modelini eğitin. Bu işlem, verinin büyüklüğüne bağlı olarak birkaç dakika sürebilir.
    ```sh
    python -m code.main --train
    ```
    Bu komut, eğitilmiş modeli `model.joblib` adıyla kaydedecektir.

3.  **Model Değerlendirme:**
    Eğitilen modelin performansını ölçmek ve GUI'de gösterilecek skor dosyasını (`model_score.json`) oluşturmak için bu komutu çalıştırın.
    ```sh
    python -m code.main --eval
    ```

4.  **Uygulamayı Başlatma:**
    Artık her şey hazır! Aşağıdaki komutla kullanıcı dostu grafiksel arayüzü başlatabilirsiniz.
    ```sh
    python gui.py
    ```

---

## 🏗️ Proje Mimarisi

Proje, görevlerin net bir şekilde ayrıldığı modüler bir yapıda tasarlanmıştır.

```
turkce_pos_tagger/
├── code/                   # Ana Python kodlarının bulunduğu paket
│   ├── core/               # Model, özellik çıkarma gibi çekirdek işlemler
│   │   ├── feature_extraction.py
│   │   ├── models.py
│   │   ├── preprocessing.py
│   │   └── tagger_system.py
│   ├── evaluation/         # Model değerlendirme kodları
│   │   └── framework.py
│   └── main.py             # Komut satırı arayüzü (CLI)
├── data/                   # Eğitim ve test verilerinin saklandığı klasör
│   ├── train/
│   └── test/
├── gui.py                  # Tkinter tabanlı grafiksel kullanıcı arayüzü
├── veri_donusturucu.py     # CoNLL-U formatını dönüştüren script
├── requirements.txt        # Proje bağımlılıkları
└── README.md               # Bu dosya
```

---

## 📜 Lisans

Bu proje, **MIT Lisansı** altında dağıtılmaktadır. Daha fazla bilgi için `LICENSE` dosyasına bakınız.

---

## 👥 Proje Ekibi

* **Ali Erdem Baltacı** - `21360859011`
* **Musa Adıgüzel** - `22360859328`
* **Nazmi Cirim** - `21360859069`
* **Siraç Gezgin** - `22360859058`

---

## 🙏 Teşekkür

* Projemizde kullandığımız veri setini sağlayan **Universal Dependencies** projesine ve **IMST Turkish Treebank** ekibine.
* Geliştirme sürecini kolaylaştıran `sklearn-crfsuite` gibi açık kaynaklı kütüphanelerin geliştiricilerine.
* Proje boyunca değerli yönlendirmelerde bulunan Dr. Öğr. Üyesi **Hayri Volkan AGUN**'a teşekkür ederiz.
