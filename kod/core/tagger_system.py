from kod.core.preprocessing import AdvancedPreprocessor
from kod.core.feature_extraction import MultiLevelFeatureExtractor
from kod.core.models import HierarchicalCRFTagger
from kod.postprocessing.consistency import ConsistencyChecker
from kod.evaluation.monitor import RealTimePerformanceMonitor

class TurkishPOSTaggerSystem:
    """
    Türkçe metinler için çok katmanlı bir POS Tagging sistemi. 
    Tüm işleme adımlarını koordine eder. Bu sınıf, sistemin ana mimarisini oluşturur. 
    """
    def __init__(self, config):
        self.config = config
        self.initialize_components()

    def initialize_components(self):
        """Sistem bileşenlerini başlatır ve modüler yapıyı kurar. """
        print("Sistem bileşenleri başlatılıyor...")
        # Çekirdek işleme bileşenleri
        self.preprocessor = AdvancedPreprocessor(self.config.preprocessing)
        self.feature_extractor = MultiLevelFeatureExtractor(self.config.features)
        
        # Makine öğrenmesi bileşeni (Model)
        self.tagger_model = HierarchicalCRFTagger(self.config.model)
        
        # Son işleme ve doğrulama bileşenleri
        self.consistency_checker = ConsistencyChecker()
        self.performance_monitor = RealTimePerformanceMonitor(self.config.monitoring)
        print("Bileşenler başarıyla başlatıldı.")

    def process_sentence(self, sentence: str) -> list:
        """
        Tek bir cümleyi işlemek için tam otomatik bir pipeline çalıştırır. 
        """
        # 1. Ön İşleme: Tokenizasyon ve Normalizasyon
        tokens = self.preprocessor.tokenize_and_normalize(sentence)

        # 2. Özellik Çıkarma: Çok seviyeli özelliklerin çıkarımı
        features = self.feature_extractor.extract_comprehensive_features(tokens)

        # 3. Tahmin (Etiketleme): Hiyerarşik model ile tahmin
        predictions = self.tagger_model.predict_hierarchical(features)

        # 4. Son İşleme: Tutarlılık kontrolü ve kural tabanlı düzeltmeler
        validated_predictions = self.consistency_checker.apply_consistency_rules(predictions)

        # 5. Performans İzleme (simülasyon)
        self.performance_monitor.monitor_prediction_quality(validated_predictions)

        # Çıktıyı daha kullanışlı bir formata dönüştür
        output = []
        for i, token_data in enumerate(validated_predictions):
            output.append({
                "id": i + 1,
                "word": tokens[i],
                "lemma": token_data['lemma'],
                "pos_tag": token_data['pos_tag'],
            })

        return output