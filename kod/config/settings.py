from types import SimpleNamespace

def load_config():
    """
    Proje yapılandırmasını yükler ve bir SimpleNamespace nesnesi olarak döndürür.
    Bu, ayarlara `config.preprocessing.lower_case` gibi kolayca erişim sağlar.
    """
    config = SimpleNamespace(
        # Ön işleme ayarları
        preprocessing=SimpleNamespace(
            lower_case=True,
            remove_punctuation=False
        ),
        
        # Özellik çıkarma ayarları
        features=SimpleNamespace(
            window_size=2,          # Bağlamsal özellikler için pencere boyutu
            use_morphological=True
        ),
        
        # Model parametreleri (CRF için)
        model=SimpleNamespace(
            algorithm='lbfgs',      # CRF'in kullanacağı optimizasyon algoritması
            c1=0.1,                 # L1 düzenlileştirme katsayısı
            c2=0.1,                 # L2 düzenlileştirme katsayısı
            max_iterations=100      # Modelin eğitimindeki maksimum iterasyon sayısı
        ),
        
        # Performans izleme ayarları
        monitoring=SimpleNamespace(
            log_performance=True    # Performans izleyici aktif mi?
        ),
        
        # Dosya yolları
        paths=SimpleNamespace(
            data_dir='../data/',
            model_save_path='../models/pos_tagger.pkl' # Eğitilmiş modelin kaydedileceği yer
        )
    )
    return config