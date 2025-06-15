# code/main.py

import sys
import json # JSON kütüphanesini ekle
from code.config import settings
from code.core import preprocessing, feature_extraction, models
from code.evaluation import framework
from code.core.tagger_system import TaggerSystem

def run_training():
    """Veri setini kullanarak modeli eğitir."""
    print("--- EĞİTİM SÜRECİ BAŞLATILDI ---")
    train_sentences = preprocessing.load_data(settings.TRAIN_DATA_PATH)
    if not train_sentences:
        return

    X_train = [feature_extraction.sentence2features(preprocessing.get_tokens_from_tagged(s)) for s in train_sentences]
    y_train = [preprocessing.get_labels_from_tagged(s) for s in train_sentences]
    
    models.train_and_save_model(X_train, y_train)

def run_evaluation():
    """
    Eğitilmiş modeli test verisiyle değerlendirir ve skoru dosyaya kaydeder.
    GÜNCELLENDİ: Artık skoru JSON dosyasına yazıyor.
    """
    print("--- DEĞERLENDİRME SÜRECİ BAŞLATILDI ---")
    model = models.load_model()
    if not model:
        return
        
    test_sentences = preprocessing.load_data(settings.TEST_DATA_PATH)
    if not test_sentences:
        return

    X_test = [feature_extraction.sentence2features(preprocessing.get_tokens_from_tagged(s)) for s in test_sentences]
    y_test = [preprocessing.get_labels_from_tagged(s) for s in test_sentences]
    
    # Değerlendirme fonksiyonundan skorları al
    scores = framework.evaluate_model(model, X_test, y_test)
    
    # Projenin ana dizininde score dosyasını oluştur
    score_file_path = "model_score.json"
    with open(score_file_path, 'w', encoding='utf-8') as f:
        json.dump(scores, f, indent=4)
    print(f"\nModel skorları '{score_file_path}' dosyasına kaydedildi.")

def run_tagging(sentence):
    """Verilen bir cümleyi etiketler."""
    print("--- ETİKETLEME SÜRECİ BAŞLATILDI ---")
    tagger = TaggerSystem()
    tagged_list = tagger.tag_sentence(sentence)
    result = tagger.format_output_string(tagged_list)
    print(f"\nCümle: '{sentence}'")
    print(f"Sonuç: {result}")

def main():
    """Ana fonksiyon. Komut satırı argümanlarını işler."""
    if len(sys.argv) < 2:
        print("Kullanım Hatası!")
        print("  Modeli eğitmek için: python -m code.main --train")
        print("  Modeli değerlendirmek için: python -m code.main --eval")
        print("  Cümle etiketlemek için: python -m code.main --tag \"cümle buraya gelecek\"")
        return

    command = sys.argv[1]

    if command == "--train":
        run_training()
    elif command == "--eval":
        run_evaluation()
    elif command == "--tag":
        if len(sys.argv) < 3:
            print("Lütfen --tag komutundan sonra etiketlenecek bir cümle girin.")
        else:
            sentence = " ".join(sys.argv[2:])
            run_tagging(sentence)
    else:
        print(f"Geçersiz komut: {command}")

if __name__ == "__main__":
    main()