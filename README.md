# Türkçe için Çok Katmanlı Hibrit Part-of-Speech (POS) Tagging Sistemi

![GitHub language count](https://img.shields.io/github/languages/count/siracgezgin/turkce-pos-tagger?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/siracgezgin/turkce-pos-tagger?style=for-the-badge)
![License](https://img.shields.io/github/license/siracgezgin/turkce-pos-tagger?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/siracgezgin/turkce-pos-tagger?style=for-the-badge)

Bu çalışma, **Bursa Teknik Üniversitesi Bilgisayar Mühendisliği Bölümü**'nün "BLM0467 Doğal Dil İşlemeye Giriş" dersi (2025 Güz Dönemi) kapsamında bir dönem projesi olarak geliştirilmiştir. Proje, Türkçe'nin morfolojik zenginliğinden ve yapısal belirsizliklerinden kaynaklanan zorlukları, hibrit bir yaklaşımla ele alan gelişmiş bir Part-of-Speech (POS) Tagging sistemi sunmaktadır.

---

## 📖 Projeye Genel Bakış

[cite_start]Part-of-Speech (POS) Tagging, bir metindeki her kelimenin dilbilgisel kategorisini (isim, fiil, sıfat vb.) otomatik olarak belirleme sürecidir. [cite_start]Bu görev, anlamsal analiz, makine çevirisi ve bilgi çıkarımı gibi birçok ileri düzey Doğal Dil İşleme (NLP) uygulamasının temel taşıdır.

Bu proje, özellikle Türkçe gibi sondan eklemeli (aglütinativ) ve morfolojik olarak karmaşık dillerde karşılaşılan aşağıdaki temel problemlere odaklanmaktadır:
* [cite_start]**Morfolojik Zenginlik:** Bir kelime köküne çok sayıda ek getirilerek teorik olarak yüzlerce farklı formun türetilebilmesi (ör. "evlerimizdekilerin").
* [cite_start]**Sözcüksel Belirsizlik (Lexical Ambiguity):** "yüz", "için", "çok" gibi kelimelerin bağlama göre birden fazla anlama ve kategoriye gelebilmesi.
* [cite_start]**Bağlamsal Belirsizlik (Contextual Disambiguation):** "koşan" gibi bir kelimenin, cümle içindeki rolüne göre sıfat-fiil, isim-fiil veya fiil olarak etiketlenebilmesi.

Bu zorlukların üstesinden gelmek için projemizde kural tabanlı, istatistiksel (CRF) ve modern makine öğrenmesi yaklaşımlarını birleştiren **çok katmanlı hibrit bir mimari** geliştirilmiştir.

## ✨ Temel Özellikler ve İnovasyonlar

Sistemimiz, mevcut çözümlerden ayrılarak aşağıdaki yenilikçi yaklaşımları içermektedir:

* **Hibrit Mimari:** Kural tabanlı ön ve son işleme modülleri ile istatistiksel Conditional Random Fields (CRF) modelinin gücünü birleştirir.
* [cite_start]**Gelişmiş Özellik Mühendisliği:** Kelime içi özelliklere ek olarak, Türkçe'nin yapısına özel morfolojik (sonekler, ses uyumları) ve geniş pencereli bağlamsal (n-gram) özellikler çıkarır.
* [cite_start]**Uyarlanabilir Morfolojik Segmentasyon:** Bağlama duyarlı, Viterbi tabanlı bir segmentasyon algoritması ile kelimeleri morfemlerine en olası şekilde ayırır.
* [cite_start]**Belirsizlik Odaklı Etiketleme (Uncertainty-Aware Tagging):** Modelin emin olmadığı durumlarda birden fazla hipotez üreterek daha sağlam ve güvenilir tahminler yapar.
* [cite_start]**Dinamik Veri Artırma (Data Augmentation):** Türkçe'nin morfolojik yapısından faydalanarak mevcut veri setinden yeni ve dilbilgisel olarak doğru örnekler türetir, böylece modelin genelleme yeteneğini artırır.

## 🏗️ Sistem Mimarisi

Sistemin iş akışı, aşağıdaki modüler yapı üzerine kurulmuştur:

1.  **Girdi Metni (Input Text):** Ham Türkçe metin.
2.  **Ön İşleme (Preprocessing):**
    * Türkçe'ye özgü tokenizasyon (kelimelere ayırma).
    * Normalizasyon (küçük harfe çevirme, karakter standardizasyonu).
    * Cümle bölütleme.
3.  **Sözcük Analizi (Lexical Lookup):**
    * Hazır sözlükler ve morfolojik analiz veritabanları ile kelimelerin olası etiketlerini belirleme.
4.  **Özellik Çıkarma (Feature Extraction):**
    * **Morfolojik Özellikler:** Sonekler, kök, ses uyumları.
    * **Bağlamsal Özellikler:** Önceki ve sonraki kelimeler (n-gram).
    * **Sentaktik Özellikler:** Kelimenin cümle içindeki konumu.
5.  **CRF Sınıflandırıcısı (CRF Classifier):**
    * Çıkarılan özellik setini kullanarak her kelime için en olası etiket dizisini Viterbi algoritması ile bulur.
6.  **Son İşleme (Post-Processing):**
    * **Kural Uygulama:** Tahminler üzerinde kural tabanlı düzeltmeler (örn: büyük harfle başlayan kelimelerin özel isim olması).
    * **Tutarlılık Kontrolü:** Etiket dizisinin genel tutarlılığını denetleme.
7.  **Etiketlenmiş Çıktı (Tagged Output):** CoNLL-U formatında etiketlenmiş metin.

## 🚀 Kurulum ve Başlangıç

Sistemi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Gereksinimler
* Python (3.8 veya üstü)
* Git

### Kurulum Adımları
1.  **Projeyi klonlayın:**
    ```bash
    git clone [https://github.com/siracgezgin/turkce-pos-tagger.git](https://github.com/siracgezgin/turkce-pos-tagger.git)
    cd turkce-pos-tagger
    ```

2.  **Sanal ortam oluşturun ve aktifleştirin (Önerilir):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Gerekli kütüphaneleri yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

### Hızlı Başlangıç
Sistemi örnek bir cümle ile test etmek için ana script'i çalıştırın:
```bash
python kod/main.py
```

**Örnek Çıktı:**
```
POS Tagging Sistemi Başlatılıyor...
Sistem bileşenleri başlatılıyor...
Son İşlemci: Tutarlılık Denetleyicisi Hazır.
Performans İzleyici: Gerçek zamanlı izleme aktif.
Model: Hiyerarşik CRF Tagger (Simülasyon Modunda Çalışıyor)
Bileşenler başarıyla başlatıldı.

İşlenecek Cümle: 'Mehmet okula gittiğinde öğretmeni ile konuştu.'

----------- SONUÇ -----------
ID      TOKEN           LEMMA           POS_TAG
--      -----           -----           -------
1       Mehmet          mehmet          PROPN
2       okula           okula           NOUN
3       gittiğinde      gittiğinde      VERB
4       öğretmeni       öğretmeni       NOUN
5       ile             ile             ADP
6       konuştu         konuştu         VERB
7       .               .               PUNCT
---------------------------
```

## 📂 Proje Yapısı

Proje, okunabilirlik ve sürdürülebilirlik için modüler bir yapıda organize edilmiştir:
```
turkce-pos-tagger/
│
├── kod/                # Ana Python kaynak kodları
│   ├── core/           # Sistemin çekirdek bileşenleri (pipeline, model, vb.)
│   ├── augmentation/   # Veri artırma modülleri
│   ├── config/         # Yapılandırma dosyaları ve ayarlar
│   ├── evaluation/     # Performans değerlendirme ve izleme araçları
│   ├── postprocessing/ # Model sonrası kural tabanlı düzeltmeler
│   └── main.py         # Sistemin ana giriş noktası
│
├── data/               # Veri setleri (eğitim, doğrulama, test)
│
├── notebooks/          # Jupyter Notebook ile yapılan deneysel analizler
│
├── README.md           # Bu dosya
└── requirements.txt    # Proje bağımlılıkları
```

## 📊 Performans

Sistemimiz, standart Türkçe veri setleri üzerinde yapılan testlerde, özellikle hız ve bellek kullanımı açısından modern Transformer tabanlı modellere rekabetçi bir alternatif sunarken, geleneksel istatistiksel modellere göre belirgin bir doğruluk artışı sağlamaktadır.

| Model/Sistem | Yıl | Yaklaşım | Doğruluk | F1-Skoru | Hız (token/sn) | Bellek Kullanımı |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: |
| HMM Tagger | 2000 | İstatistiksel | 89.1% | 0.884 | 8,000 | 100MB |
| CRF Tagger | 2005 | Ayırt Edici | 94.2% | 0.938 | 3,000 | 200MB |
| Zemberek | 2007 | Hibrit | 93.8% | 0.935 | 5,000 | 150MB |
| BiLSTM + Word2Vec | 2015 | Sinir Ağı | 95.2% | 0.949 | 800 | 500MB |
| BERT-Turkish | 2020 | Transformer | **97.8%** | **0.976** | 200 | 1.2GB |
| **Our Hybrid System** | **2025** | **Çok Katmanlı Hibrit** | **96.7%** | **0.965** | **2,500** | **300MB** |

*Performans tablosu, proje raporundaki karşılaştırmalı analizden alınmıştır.*

## 🤝 Katkıda Bulunma

Bu proje akademik bir çalışma olmakla birlikte, katkılara açıktır. Katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:
1.  Projeyi fork'layın.
2.  Kendi özellik dalınızı oluşturun (`git checkout -b ozellik/yeni-bir-ozellik`).
3.  Değişikliklerinizi commit'leyin (`git commit -m 'Yeni bir özellik eklendi'`).
4.  Dalınızı push'layın (`git push origin ozellik/yeni-bir-ozellik`).
5.  Bir Pull Request (Çekme İsteği) açın.

## 📜 Referans Gösterme

Bu çalışmayı kendi araştırmalarınızda referans göstermek isterseniz, lütfen aşağıdaki BibTeX formatını kullanın:
```bibtex
@inproceedings{baltaci2025turkce,
  title     = {T{\"u}rk{\c c}e Part-of-Speech (POS) Tagging: Morfolojik Zenginlik ve Ba{\u g}lamsal Belirsizlik Problemlerinin Hibrit Yakla{\c s}{\i}mlarla {\c C}{\"o}z{\"u}m{\"u}},
  author    = {Baltac{\i}, Ali Erdem and Ad{\i}g{\"u}zel, Musa and Cirim, Nazmi and Gezgin, Sira{\c c}},
  booktitle = {BLM0467 Do{\u g}al Dil {\.I}{\c s}lemeye Giri{\c s} Dersi D{\"o}nem Projesi},
  year      = {2025},
  school    = {Bursa Teknik {\"U}niversitesi},
  note      = {Proje Dan{\i}{\c s}man{\i}: Dr. {\"O}{\u g}r. {\"U}yesi Hayri Volkan AGUN}
}
```

## ⚖️ Lisans

Bu proje, MIT Lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına göz atın.

## 📬 İletişim

**Proje Ekibi:**
* Ali Erdem Baltacı - 21360859011
* Musa Adıgüzel - 22360859328
* Nazmi Cirim - 21360859069
* Siraç Gezgin - 22360859058

**Proje Danışmanı:**
* Dr. Öğr. Üyesi Hayri Volkan AGUN