def word2features(sentence_tokens, i):
    """Bir kelime için öznitelik sözlüğü oluşturur."""
    word = sentence_tokens[i]
    
    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word.suffix(3)': word[-3:],
        'word.suffix(2)': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
    }
    
    # Önceki kelimenin öznitelikleri
    if i > 0:
        prev_word = sentence_tokens[i-1]
        features.update({
            '-1:word.lower()': prev_word.lower(),
            '-1:word.istitle()': prev_word.istitle(),
        })
    else:
        features['BOS'] = True  # Cümlenin Başı (Beginning of Sentence)

    # Sonraki kelimenin öznitelikleri
    if i < len(sentence_tokens)-1:
        next_word = sentence_tokens[i+1]
        features.update({
            '+1:word.lower()': next_word.lower(),
            '+1:word.istitle()': next_word.istitle(),
        })
    else:
        features['EOS'] = True  # Cümlenin Sonu (End of Sentence)
        
    return features

def sentence2features(sentence_tokens):
    """Cümledeki tüm kelimeler için öznitelik listesi oluşturur."""
    return [word2features(sentence_tokens, i) for i in range(len(sentence_tokens))]