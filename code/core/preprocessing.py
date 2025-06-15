def load_data(file_path):
    """
    Verilen yoldaki etiketli veriyi okur ve cümle listesi olarak döndürür.
    Format: [ [ (kelime1, etiket1), (kelime2, etiket2) ], [ (kelimeA, etiketA) ] ]
    """
    sentences = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            sentence = []
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split()
                    if len(parts) == 2:
                        word, tag = parts
                        sentence.append((word, tag))
                    else:
                        # Boşluklu veya hatalı satırları atla
                        print(f"Hatalı satır atlandı: {line}")
                else:
                    if sentence:
                        sentences.append(sentence)
                        sentence = []
            # Dosya sonundaki son cümleyi de ekle
            if sentence:
                sentences.append(sentence)
    except FileNotFoundError:
        print(f"Hata: Veri dosyası bulunamadı -> {file_path}")
        return None
    return sentences

def tokenize_sentence(sentence_str):
    """Basit bir şekilde string'i kelimelere ayırır."""
    return sentence_str.split()

def get_tokens_from_tagged(tagged_sentence):
    """(kelime, etiket) listesinden sadece kelimeleri alır."""
    return [word for word, tag in tagged_sentence]

def get_labels_from_tagged(tagged_sentence):
    """(kelime, etiket) listesinden sadece etiketleri alır."""
    return [tag for word, tag in tagged_sentence]