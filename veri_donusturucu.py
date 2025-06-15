import sys

def convert_conllu_to_pos(input_file, output_file):
    """
    Universal Dependencies .conllu dosyasını okur ve
    'kelime ETİKET' formatında bir .txt dosyası oluşturur.
    """
    print(f"'{input_file}' dosyası okunuyor...")
    
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            # Yorum satırlarını atla
            if line.startswith('#'):
                continue
            # Cümleler arası boş satırları koru
            if line.strip() == '':
                f_out.write('\n')
                continue
            
            parts = line.split('\t')
            # Geçerli bir satır olup olmadığını kontrol et (en az 10 sütun olmalı)
            if len(parts) >= 4:
                # 2. sütun kelime (FORM), 4. sütun etiket (UPOS)
                word = parts[1]
                tag = parts[3]
                
                # Çok kelimeli ifadeleri atla (örn: 1-2 gidiyor)
                if '-' not in parts[0]:
                    f_out.write(f"{word} {tag}\n")

    print(f"Dönüştürme tamamlandı. Sonuç: '{output_file}'")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Kullanım: python veri_donusturucu.py <girdi_dosyasi.conllu> <cikti_dosyasi.txt>")
        sys.exit(1)
        
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    convert_conllu_to_pos(input_path, output_path)