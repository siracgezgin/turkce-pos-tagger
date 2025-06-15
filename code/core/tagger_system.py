from code.core.models import load_model
from code.core.preprocessing import tokenize_sentence
from code.core.feature_extraction import sentence2features

class TaggerSystem:
    def __init__(self):
        self.model = load_model()

    def tag_sentence(self, sentence_str):
        """
        Verilen bir string cümleyi etiketler ve (kelime, etiket) listesi döndürür.
        BU METOT GÜNCELLENDİ.
        """
        if not self.model:
            print("Model yüklenemedi.")
            return []
            
        tokens = tokenize_sentence(sentence_str)
        features = sentence2features(tokens)
        tags = self.model.predict([features])[0]
        
        # Formatlı string yerine (kelime, etiket) çiftlerinden oluşan bir liste döndür
        tagged_sentence_list = list(zip(tokens, tags))
        return tagged_sentence_list

    def format_output_string(self, tagged_sentence_list):
        """Komut satırı için eski formatlı çıktıyı üreten yardımcı metot."""
        return " ".join([f"{word}/{tag}" for word, tag in tagged_sentence_list])