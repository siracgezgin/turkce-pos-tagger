import os

# Projenin ana dizinini programatik olarak bulur.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Veri setlerinin yolları
TRAIN_DATA_PATH = os.path.join(BASE_DIR, 'data', 'train', 'corpus.txt')
TEST_DATA_PATH = os.path.join(BASE_DIR, 'data', 'test', 'corpus.txt')

# Eğitilmiş modelin kaydedileceği yol
MODEL_SAVE_PATH = os.path.join(BASE_DIR, 'model.joblib')