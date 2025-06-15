import re
import locale

class AdvancedPreprocessor:
    """
    Türkçe metinler için gelişmiş ön işleme adımlarını uygular. 
    Bu sınıf, metni token'lara ayırma ve standartlaştırma görevlerini içerir.
    """
    def __init__(self, config):
        self.config = config
        # Türkçe yerel ayarlarını etkinleştirmeye çalışır. Bu, özellikle
        # büyük/küçük harf dönüşümlerinin doğru çalışması için önemlidir.
        try:
            locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')
        except locale.Error:
            print("Uyarı: 'tr_TR.UTF-8' yerel ayarı desteklenmiyor. Standart metotlar kullanılacak.")

    def tokenize_and_normalize(self, text: str) -> list:
        """Tokenizasyon ve normalizasyon işlemlerini bir arada yürüten ana metot."""
        normalized_text = self._normalize(text)
        tokens = self._tokenize(normalized_text)
        return tokens

    def _normalize(self, text: str) -> str:
        """
        Metni standart bir forma getirir. Türkçe'ye özgü karakterleri ve
        büyük/küçük harf dönüşümlerini ele alır. 
        """
        # Türkçe'ye özgü karakter dönüşüm haritası
        char_mappings = {
            'İ': 'i', 'I': 'ı', 'Ğ': 'ğ', 'Ü': 'ü', 'Ş': 'ş', 'Ö': 'ö', 'Ç': 'ç'
        }
        
        # Önce büyük harfleri küçük harf karşılıkları ile değiştir
        for upper, lower in char_mappings.items():
            text = text.replace(upper, lower)
        
        # Metnin tamamını küçük harfe çevir
        text = text.lower()

        # Sosyal medya metinlerinde sık görülen karakter tekrarlarını azaltır (ör: "çooook" -> "çook") 
        text = re.sub(r'(.)\1{2,}', r'\1\1', text)
        
        return text

    def _tokenize(self, text: str) -> list:
        """
        Metni kelimelere (token) ve noktalama işaretlerine ayırır.
        Bu işlem, Türkçe'nin yapısına uygun, sınırlara duyarlı bir şekilde yapılır. 
        """
        # Kelimeleri (ve apostrofları) veya tek başına noktalama işaretlerini bulan bir regex
        # Örnek: "Mehmet'in, evi." -> ["Mehmet'in", ",", "evi", "."]
        tokens = re.findall(r"[\w']+|[.,!?;:]", text)
        return tokens