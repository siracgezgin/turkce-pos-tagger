class ConsistencyChecker:
    """
    Model tarafından üretilen etiket dizileri üzerinde tutarlılık kontrolleri
    ve kural tabanlı düzeltmeler uygular.
    """
    def __init__(self):
        # Gerçek bir sistemde, sık kullanılan kelimeler gibi listeler burada yüklenebilir.
        # self.common_words = load_common_words()
        print("Son İşlemci: Tutarlılık Denetleyicisi Hazır.")

    def apply_consistency_rules(self, tagged_sequence: list) -> list:
        """
        Tüm tutarlılık kurallarını sırasıyla uygular.
        """
        # Kuralları bir liste içinde tanımlayarak kolayca genişletilebilir hale getiririz.
        rules = [
            self._check_proper_noun_capitalization
            # Gelecekte buraya yeni kurallar eklenebilir.
            # self._check_verb_agreement,
            # self._check_case_agreement,
        ]

        # Her kuralı sırayla uygula
        for rule in rules:
            tagged_sequence = rule(tagged_sequence)
            
        return tagged_sequence

    def _check_proper_noun_capitalization(self, sequence: list) -> list:
        """
        Büyük harfle başlayan kelimeler için bir özel isim (PROPN) kontrolü yapar.
        Eğer bir kelime büyük harfle başlıyorsa ve cümlenin ilk kelimesi değilse,
        etiketinin 'PROPN' olma olasılığı yüksektir.
        """
        # Dizi kopyası üzerinde çalışarak orijinal veriyi bozmuyoruz.
        corrected_sequence = sequence.copy()

        for i, token_data in enumerate(corrected_sequence):
            # Orijinal kelimeyi özellikler içerisinden alalım
            word = token_data['features']['word.lower()'] # Aslında orijinal hali lazım
            # Orijinal token'ı bulmak için daha iyi bir yol gerekebilir,
            # şimdilik simülasyon için title kontrolü yapalım.
            is_title = token_data['features']['word.istitle()']
            is_bos = token_data['features'].get('BOS', False) # Cümle başı mı?

            # Eğer kelime büyük harfle başlıyorsa VE cümlenin ilk kelimesi değilse
            if is_title and not is_bos:
                # Ve mevcut etiketi PROPN değilse, onu PROPN olarak düzelt.
                if token_data['pos_tag'] != 'PROPN':
                    # print(f"Düzeltme: '{word}' kelimesi PROPN olarak etiketlendi.")
                    corrected_sequence[i]['pos_tag'] = 'PROPN'
                    
        return corrected_sequence