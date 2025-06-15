from .preprocessing import AdvancedPreprocessor
from .feature_extraction import MultiLevelFeatureExtractor
from .models import HierarchicalCRFTagger
from ..postprocessing.consistency import ConsistencyChecker
from ..evaluation.monitor import RealTimePerformanceMonitor

class TurkishPOSTaggerSystem:
    """
    Türkçe metinler için çok katmanlı bir POS Tagging sistemi.
    Tüm işleme adımlarını koordine eder.
    """
    def __init__(self, config):
        self.config = config
        self.initialize_components()

    def initialize_components(self):
        """Sistem bileşenlerini başlatır."""
        print("Sistem bileşenleri başlatılıyor...")
        self.preprocessor = AdvancedPreprocessor(self.config.preprocessing)
        self.feature_extractor = MultiLevelFeatureExtractor(self.config.features)
        self.tagger_model = HierarchicalCRFTagger(self.config.model)
        self.consistency_checker = ConsistencyChecker()
        self.performance_monitor = RealTimePerformanceMonitor(self.config.monitoring)
        print("Bileşenler başarıyla başlatıldı.")

    def process_sentence(self, sentence: str) -> list:
        """
        Tek bir cümleyi işlemek için tam bir pipeline çalıştırır.
        """
        # 1. Ön İşleme
        tokens = self.preprocessor.tokenize_and_normalize(sentence)

        # 2. Özellik Çıkarma
        features = self.feature_extractor.extract_comprehensive_features(tokens)

        # 3. Tahmin (Etiketleme)
        predictions = self.tagger_model.predict_hierarchical(features)

        # 4. Son İşleme ve Tutarlılık Kontrolü
        validated_predictions = self.consistency_checker.apply_consistency_rules(predictions)

        # 5. Performans İzleme (simülasyon)
        self.performance_monitor.monitor_prediction_quality(validated_predictions)

        # Çıktıyı formatla
        output = []
        for i, token in enumerate(tokens):
            output.append({
                "id": i + 1,
                "word": token,
                "lemma": validated_predictions[i]['lemma'],
                "pos_tag": validated_predictions[i]['pos_tag'],
            })

        return output