import joblib
import sklearn_crfsuite
from code.config import settings


def train_and_save_model(X_train, y_train):
    """CRF modelini eğitir ve belirtilen yola kaydeder."""
    print("Model eğitimi başlıyor...")
    crf = sklearn_crfsuite.CRF(
        algorithm='lbfgs',
        c1=0.1,
        c2=0.1,
        max_iterations=100,
        all_possible_transitions=True
    )
    crf.fit(X_train, y_train)
    
    print(f"Model şuraya kaydediliyor: {settings.MODEL_SAVE_PATH}")
    joblib.dump(crf, settings.MODEL_SAVE_PATH)
    print("Model başarıyla eğitildi ve kaydedildi.")
    return crf

def load_model():
    """Kaydedilmiş modeli yükler."""
    try:
        model = joblib.load(settings.MODEL_SAVE_PATH)
        print("Model başarıyla yüklendi.")
        return model
    except FileNotFoundError:
        print(f"Hata: Kayıtlı model bulunamadı -> {settings.MODEL_SAVE_PATH}")
        print("Lütfen önce modeli --train komutuyla eğitin.")
        return None