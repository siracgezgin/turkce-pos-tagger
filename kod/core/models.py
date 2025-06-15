# Gerçek bir proje için `pip install sklearn-crfsuite` komutu ile bu kütüphaneyi
# yüklemeniz ve modeli eğitmeniz gerekir. Biz burada bu adımı simüle ediyoruz.
# import sklearn_crfsuite

class HierarchicalCRFTagger:
    """
    Hiyerarşik bir CRF modeli (Coarse ve Fine-grained) için bir iskelet.
    Bu sınıf, gerçek bir modelin eğitilmesini ve tahmin yapmasını simüle eder.
    """
    def __init__(self, config):
        self.config = config
        # Gerçek bir model burada yüklenirdi veya başlatılırdı.
        # self.model = sklearn_crfsuite.CRF(...)
        # self.model.fit(X_train, y_train) # Eğitim adımı
        print("Model: Hiyerarşik CRF Tagger (Simülasyon Modunda Çalışıyor)")

    def predict_hierarchical(self, sentence_features: list) -> list:
        """
        Verilen özelliklere dayanarak hiyerarşik etiketleme yapar (simülasyon).

        Bu metot, eğitilmiş bir modelin davranışını basit kurallarla taklit eder.
        Gelen kelimelere bakarak onlara bir POS etiketi ve kök (lemma) atar.
        """
        predictions = []
        for features in sentence_features:
            word = features['word.lower()']
            
            # Basit kural tabanlı tahminler
            pos_tag = 'NOUN'  # Varsayılan etiket
            lemma = word     # Varsayılan kök

            if word in ['gitti', 'konuştu', 'geldi', 'koşan', 'kaybolmuş']:
                pos_tag = 'VERB'
            elif word in ['okula', 'öğretmeni', 'ev', 'anahtar', 'kişi', 'yüzü']:
                pos_tag = 'NOUN'
            elif word in ['mehmet', 'türkiye', 'istanbul']:
                pos_tag = 'PROPN' # Özel İsim
            elif word in ['ile', 'için', 'kadar']:
                pos_tag = 'ADP'   # Edat
            elif word in ['güzeldi', 'büyük', 'kırmızı']:
                pos_tag = 'ADJ' # Sıfat
            elif word == 'çok':
                pos_tag = 'ADV' # Zarf
            elif word.isdigit() or word == 'yüz': # "yüz" kelimesinin sayı anlamı
                 if features.get('next_word.lower()') == 'kişi':
                     pos_tag = 'NUM' # Sayı
            elif features.get('BOS', False) and features.get('word.istitle()', False):
                 pos_tag = 'PROPN'
            elif features.get('EOS', False) and word in ['.', '!', '?']:
                 pos_tag = 'PUNCT' # Noktalama

            predictions.append({
                'pos_tag': pos_tag,
                'lemma': lemma, # Simülasyon için kök bulma basitleştirildi
                'features': features
            })
        return predictions