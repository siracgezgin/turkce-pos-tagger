class MultiLevelFeatureExtractor:
    """
    Token dizisinden çok seviyeli (morfolojik, bağlamsal, vb.)
    özellikler çıkarır.
    """
    def __init__(self, config):
        self.config = config

    def extract_comprehensive_features(self, tokens: list) -> list:
        """Tüm özellik çıkarma adımlarını yönetir."""
        sentence_features = []
        for i in range(len(tokens)):
            features = {}
            word = tokens[i]
            # Temel özellikler
            features.update(self._get_word_level_features(word))
            # Bağlamsal özellikler
            features.update(self._get_contextual_features(tokens, i))
            # Morfolojik özellikler (simüle edilmiş)
            features.update(self._get_morphological_features(word))
            sentence_features.append(features)
        return sentence_features

    def _get_word_level_features(self, word: str) -> dict:
        """Kelime seviyesinde temel özellikleri çıkarır."""
        return {
            'word.lower()': word.lower(),
            'word[-3:]': word[-3:],
            'word[-2:]': word[-2:],
            'word.isupper()': word.isupper(),
            'word.istitle()': word.istitle(),
            'word.isdigit()': word.isdigit(),
            'length': len(word)
        }

    def _get_contextual_features(self, tokens: list, index: int) -> dict:
        """Pencereleme yöntemiyle bağlamsal özellikleri çıkarır."""
        features = {}
        features['prev_word'] = tokens[index-1] if index > 0 else '<START>'
        features['next_word'] = tokens[index+1] if index < len(tokens)-1 else '<END>'
        return features

    def _get_morphological_features(self, word: str) -> dict:
        """Simüle edilmiş morfolojik özellikleri çıkarır."""
        features = {}
        # Basit sonek kontrolleri
        if word.endswith('ler') or word.endswith('lar'):
            features['is_plural'] = True
        if word.endswith('de') or word.endswith('da'):
            features['has_locative_case'] = True
        return features