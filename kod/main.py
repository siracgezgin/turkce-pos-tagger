import sys
from pathlib import Path

# Proje kök dizinini Python'un modül arama yoluna ekler.
# Bu, diğer klasörlerdeki modülleri import etmemizi sağlar.
sys.path.append(str(Path(__file__).resolve().parent.parent))

from kod.core.tagger_system import TurkishPOSTaggerSystem
from kod.config.settings import load_config

def main():
    """
    Ana fonksiyon: Yapılandırmayı yükler, POS Tagger sistemini başlatır
    ve örnek bir metni işler.
    """
    print("POS Tagging Sistemi Başlatılıyor...")
    
    # Proje yapılandırmasını yükle
    config = load_config()

    # Tagger sistemini başlat
    tagger = TurkishPOSTaggerSystem(config)

    # Örnek bir cümle belirle 
    sentence = "Mehmet okula gittiğinde öğretmeni ile konuştu."
    print(f"\nİşlenecek Cümle: '{sentence}'")

    # Cümleyi etiketle
    tagged_sentence = tagger.process_sentence(sentence)

    # Sonuçları daha okunaklı bir formatta yazdır
    print("\n----------- SONUÇ -----------")
    print("ID\tTOKEN\t\tLEMMA\t\tPOS_TAG")
    print("--\t-----\t\t-----\t\t-------")
    for token_info in tagged_sentence:
        # Token ve lemma'yı belirli bir uzunlukta tutarak hizalamayı iyileştir
        word = token_info['word'][:12]
        lemma = token_info['lemma'][:12]
        print(f"{token_info['id']}\t{word:<12}\t{lemma:<12}\t{token_info['pos_tag']}")
    print("---------------------------\n")


if __name__ == "__main__":
    # Bu script doğrudan çalıştırıldığında main() fonksiyonunu çağırır.
    main()