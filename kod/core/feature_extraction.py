class MultiLevelFeatureExtractor:
    """
    Token dizisinden çok seviyeli (kelime bazlı, morfolojik, bağlamsal)
    özellikler çıkarır. Bu özellikler, CRF modelini beslemek için kullanılır.
    """
    def __init__(self, config):
        self.config = config
        self.window_size = config.features.window_size

    def extract_comprehensive_features(self, tokens: list) -> list:
        """
        Bir cümledeki tüm token'lar için özellik listesi oluşturan ana metot.
        """
        sentence_features = []
        for i in range(len(tokens)):
            # Her bir token için tüm özellikleri tek bir sözlükte birleştirir.
            features = {}
            word = tokens[i]
            features.update(self._get_word_level_features(word))
            features.update(self._get_contextual_features(tokens, i))
            features.update(self._get_morphological_features(word)) # Simüle edilmiş
            sentence_features.append(features)
        return sentence_features

    def _get_word_level_features(self, word: str) -> dict:
        """
        Tek bir kelimenin kendi içindeki özelliklerini çıkarır.
        Örnek: kelimenin kendisi, son ekleri, büyük/küçük harf durumu vb.
        """
        return {
            'bias': 1.0, # Her zaman 1 olan bir yanlılık terimi, modelin öğrenmesine yardımcı olur.
            'word.lower()': word.lower(),
            'word[-3:]': word[-3:],
            'word[-2:]': word[-2:],
            'word.isupper()': word.isupper(),
            'word.istitle()': word.istitle(),
            'word.isdigit()': word.isdigit(),
            'word.length': len(word),
        }

    def _get_contextual_features(self, tokens: list, index: int) -> dict:
        """
        Belirli bir kelimenin bağlamından (önceki ve sonraki kelimeler)
        özellikler çıkarır.
        """
        features = {}
        # Önceki kelimeler için özellikler
        if index > 0:
            prev_word = tokens[index-1]
            features['prev_word.lower()'] = prev_word.lower()
            features['prev_word.istitle()'] = prev_word.istitle()
            features['prev_word.isupper()'] = prev_word.isupper()
        else:
            features['BOS'] = True # 'Beginning of Sentence' (Cümle Başı)

        # Sonraki kelimeler için özellikler
        if index < len(tokens)-1:
            next_word = tokens[index+1]
            features['next_word.lower()'] = next_word.lower()
            features['next_word.istitle()'] = next_word.istitle()
            features['next_word.isupper()'] = next_word.isupper()
        else:
            features['EOS'] = True # 'End of Sentence' (Cümle Sonu)

        return features

    def _get_morphological_features(self, word: str) -> dict:
        """
        (Simüle edilmiş) Morfolojik özellikleri çıkarır. Gerçek bir sistemde
        bu kısım çok daha karmaşık olur ve bir morfolojik analiz aracı kullanırdı.
        """
        features = {}
        # Türkçe'de sık görülen bazı ekleri kontrol et
        if len(word) > 4:
            if word.lower().endswith('ler') or word.lower().endswith('lar'):
                features['is_plural'] = True
            if word.lower().endswith('de') or word.lower().endswith('da'):
                features['has_locative_case'] = True # Bulunma hali
            if word.lower().endswith('den') or word.lower().endswith('dan'):
                features['has_ablative_case'] = True # Ayrılma hali
        return features