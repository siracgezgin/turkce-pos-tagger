import sys
from pathlib import Path

# Proje kök dizinini Python yoluna ekle
sys.path.append(str(Path(__file__).parent.parent))

from kod.core.tagger_system import TurkishPOSTaggerSystem
from kod.config.settings import load_config

def main():
    """
    Ana fonksiyon: Yapılandırmayı yükler, POS Tagger sistemini başlatır
    ve örnek bir metni işler.
    """
    # Yapılandırma dosyasını yükle
    config_path = Path(__file__).parent / 'config' / 'settings.py'
    config = load_config(config_path)

    # Tagger sistemini başlat
    tagger = TurkishPOSTaggerSystem(config)

    # Örnek bir cümleyi işle
    sentence = "Mehmet okula gittiğinde öğretmeni ile konuştu."
    print(f"Girdi Cümlesi: {sentence}\n")

    # Cümleyi etiketle
    tagged_sentence = tagger.process_sentence(sentence)

    # Sonuçları yazdır
    print("Etiketlenmiş Çıktı (CoNLL-U Benzeri Format):")
    for token_info in tagged_sentence:
        print(f"{token_info['id']}\t{token_info['word']}\t{token_info['lemma']}\t{token_info['pos_tag']}\t...")

if __name__ == "__main__":
    main()