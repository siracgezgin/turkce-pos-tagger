import re
import locale

class AdvancedPreprocessor:
    """
    Türkçe metinler için gelişmiş ön işleme adımlarını uygular.
    """
    def __init__(self, config):
        self.config = config
        # Türkçe yerel ayarlarını etkinleştirme
        try:
            locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')
        except locale.Error:
            print("Uyarı: 'tr_TR.UTF-8' yerel ayarı desteklenmiyor. Standart lower() kullanılacak.")


    def tokenize_and_normalize(self, text: str) -> list:
        """Tokenizasyon ve normalizasyon işlemlerini bir arada yürütür."""
        normalized_text = self._normalize(text)
        tokens = self._tokenize(normalized_text)
        return tokens

    def _normalize(self, text: str) -> str:
        """Metni standart bir forma getirir."""
        # Karakter normalizasyonu
        char_mappings = {'İ': 'i', 'I': 'ı', 'Ğ': 'ğ', 'Ü': 'ü', 'Ş': 'ş', 'Ö': 'ö', 'Ç': 'ç'}
        for upper, lower in char_mappings.items():
            text = text.replace(upper, lower)
        
        # Küçük harfe çevirme
        text = text.lower()

        # Sosyal medya metinlerine özgü normalizasyonlar
        text = re.sub(r'(.)\1{2,}', r'\1\1', text)  # "çooook" -> "çook"
        return text

    def _tokenize(self, text: str) -> list:
        """Metni kelimelere (token) ayırır."""
        # Noktalama işaretlerini koruyarak ayırma
        tokens = re.findall(r"[\w']+|[.,!?;:]", text)
        return tokens