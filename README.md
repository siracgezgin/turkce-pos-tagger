# Türkçe Metinler için Çok Katmanlı Part-of-Speech (POS) Tagging Sistemi

Bu proje, Bursa Teknik Üniversitesi Bilgisayar Mühendisliği Bölümü, BLM0467 Doğal Dil İşlemeye Giriş dersi kapsamında geliştirilmiştir. Projenin amacı, Türkçe'nin morfolojik zenginliği ve bağlamsal belirsizlik gibi zorluklarını ele alan hibrit bir Part-of-Speech (POS) Tagging sistemi geliştirmektir.

## Proje Hakkında

Bu sistem, kural tabanlı, istatistiksel ve sinir ağı yaklaşımlarını bir araya getiren çok katmanlı bir hibrit mimari kullanmaktadır. Raporda detaylandırılan bu mimari, aşağıdaki temel adımları içerir:

1.  **Gelişmiş Ön İşleme:** Türkçe'ye özgü normalizasyon ve tokenizasyon.
2.  **Çok Seviyeli Özellik Çıkarma:** Morfolojik, bağlamsal ve sentaktik özelliklerin çıkarımı.
3.  **Hiyerarşik CRF Modeli:** Kelimeleri önce genel (coarse-grained) sonra daha detaylı (fine-grained) olarak etiketleyen bir model.
4.  **Son İşleme:** Kural tabanlı kontroller ile model çıktılarının tutarlılığının artırılması.

## Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

1.  **Repoyu Klonlayın:**
    ```bash
    git clone <repo-adresi>
    cd turkce_pos_tagger
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    Bir sanal ortam (virtual environment) oluşturmanız önerilir.
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows

    pip install -r requirements.txt
    ```

## Kullanım

Sistemi çalıştırmak için `kod` klasörü içindeki `main.py` dosyasını kullanabilirsiniz:

```bash
python kod/main.py