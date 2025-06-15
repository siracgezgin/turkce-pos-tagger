# code/evaluation/framework.py

from sklearn_crfsuite import metrics

def evaluate_model(crf_model, X_test, y_test):
    """
    Modeli test verisi üzerinde değerlendirir, raporu basar ve skorları döndürür.
    GÜNCELLENDİ: Artık skorları return ediyor.
    """
    print("\nModel Değerlendirme Raporu:")
    
    labels = list(crf_model.classes_)
    y_pred = crf_model.predict(X_test)
    
    # Skorları hesapla
    accuracy = metrics.flat_accuracy_score(y_test, y_pred)
    f1_score = metrics.flat_f1_score(y_test, y_pred, average='weighted', labels=labels)
    
    print(f"Genel Doğruluk (Accuracy): {accuracy:.4f}")
    print(f"Genel F1 Skoru (Weighted): {f1_score:.4f}")
    
    report = metrics.flat_classification_report(
        y_test, y_pred, labels=labels, digits=3
    )
    print("\nEtiketlere Göre Detaylı Rapor:")
    print(report)

    # Hesaplanan skorları bir sözlük olarak döndür
    return {'accuracy': accuracy, 'f1_score': f1_score}