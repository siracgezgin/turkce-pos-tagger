import random

class MorphologicalDataAugmenter:
    """
    Morfolojik varyasyonlar yaratarak eğitim veri setini genişletir (simülasyon).
    Bu, modelin morfolojik olarak zengin dillerde daha iyi genelleme yapmasına yardımcı olur.
    """
    def __init__(self):
        print("Veri Artırıcı: Morfolojik artırma modülü hazır.")
        # Gerçek bir sistemde, morfolojik kurallar ve ekler burada yüklenebilirdi.
        self.case_suffixes = ['e', 'i', 'de', 'den']
        self.plural_suffix = 'ler'

    def augment_training_data(self, original_dataset, augmentation_factor=2):
        """
        Veri setini morfolojik varyasyonlarla genişleten ana metot (simülasyon).
        """
        print(f"\n--- Veri Artırma Başlatılıyor (Faktör: {augmentation_factor}) ---")
        augmented_data = []
        # for sentence, tags in original_dataset:
        #     augmented_data.append((sentence, tags)) # Orijinali ekle
            
        #     for _ in range(augmentation_factor):
        #         variant_sentence, variant_tags = self._generate_sentence_variant(sentence, tags)
        #         augmented_data.append((variant_sentence, variant_tags))
        
        print("--- Veri Artırma Tamamlandı ---\n")
        # return augmented_data
        return original_dataset # Simülasyon olduğu için orijinal veriyi döndürüyoruz.


    def _generate_sentence_variant(self, sentence, tags):
        """Tek bir cümlenin varyantını oluşturur (simülasyon)."""
        variant_sentence = []
        variant_tags = []
        
        for word, tag in zip(sentence, tags):
            # Sadece isim ve fiiller üzerinde değişiklik yapmayı seçelim
            if tag in ['NOUN', 'VERB'] and random.random() > 0.5:
                variant_word = self._generate_morphological_variant(word, tag)
                variant_sentence.append(variant_word)
                variant_tags.append(tag) # Etiket aynı kalır
            else:
                variant_sentence.append(word)
                variant_tags.append(tag)
                
        return variant_sentence, variant_tags

    def _generate_morphological_variant(self, word, pos_tag):
        """Belirli bir kelime için morfolojik varyant üretir (simülasyon)."""
        if pos_tag == 'NOUN':
            # Rastgele bir durum eki ekle veya çoğul yap
            if random.random() > 0.5:
                return word + random.choice(self.case_suffixes)
            else:
                # Basit bir çoğul yapma kuralı (ses uyumları göz ardı edilmiştir)
                return word + self.plural_suffix
        
        # Diğer POS etiketleri için de benzer kurallar eklenebilir.
        return word