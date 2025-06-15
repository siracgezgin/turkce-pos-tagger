# gui.py

import tkinter as tk
from tkinter import font
import json
import random
from code.core.tagger_system import TaggerSystem

# ETİKETLER İÇİN TÜRKÇE VE RENK HARİTASI
TAG_MAP = {
    'NOUN':   {'tr': 'İsim', 'color': '#a7d2e8'},
    'VERB':   {'tr': 'Fiil', 'color': '#b3e8a7'},
    'ADJ':    {'tr': 'Sıfat', 'color': '#e8d1a7'},
    'ADV':    {'tr': 'Zarf', 'color': '#e8a7c3'},
    'PRON':   {'tr': 'Zamir', 'color': '#d8a7e8'},
    'PROPN':  {'tr': 'Özel İsim', 'color': '#a7bde8'},
    'DET':    {'tr': 'Belirteç', 'color': '#e8e5a7'},
    'NUM':    {'tr': 'Sayı', 'color': '#f0c27b'},
    'ADP':    {'tr': 'Edat', 'color': '#a7e8e8'},
    'AUX':    {'tr': 'Yardımcı Fiil', 'color': '#b3e8a7'},
    'CONJ':   {'tr': 'Bağlaç', 'color': '#e8c8a7'},
    'CCONJ':  {'tr': 'Bağlaç', 'color': '#e8c8a7'},
    'SCONJ':  {'tr': 'Bağlaç', 'color': '#e8c8a7'},
    'PUNCT':  {'tr': 'Noktalama', 'color': '#d3d3d3'},
    'INTJ':   {'tr': 'Ünlem', 'color': '#e8a7a7'},
    'PART':   {'tr': 'Parçacık', 'color': '#c8a7e8'},
    'SYM':    {'tr': 'Sembol', 'color': '#d3d3d3'},
    'X':      {'tr': 'Diğer', 'color': '#f5f5f5'},
    'default':{'tr': 'Bilinmeyen', 'color': '#f5f5f5'}
}

# Örnek cümleler listesi
EXAMPLE_SENTENCES = [
    "Türkiye'nin en kalabalık şehri İstanbul'dur.",
    "Kırmızı araba yavaşça gözden kayboldu.",
    "Eğer proje zamanında biterse tatile çıkacağız.",
    "Bu kitabı ve diğerlerini de okudun mu?",
    "Eyvah! Anahtarları içeride unuttum."
]

# --- Tagger Sistemini Yükleme ---
print("Model yükleniyor, lütfen bekleyin...")
tagger = TaggerSystem()
print("Model yüklendi. Arayüz hazır.")

# --- FONKSİYONLAR ---
def load_model_score():
    try:
        with open("model_score.json", 'r', encoding='utf-8') as f:
            scores = json.load(f)
            accuracy = scores.get('accuracy', 0)
            status_var.set(f"Model Doğruluk Oranı: %{accuracy*100:.2f}")
    except FileNotFoundError:
        status_var.set("Model henüz değerlendirilmedi. Lütfen --eval komutunu çalıştırın.")

def handle_tag_button_click():
    input_sentence = entry_sentence.get()
    
    # Önceki sonuçları temizle
    for widget in results_frame.winfo_children():
        widget.destroy()

    if input_sentence:
        tagged_list = tagger.tag_sentence(input_sentence)
        
        for word, tag in tagged_list:
            tag_info = TAG_MAP.get(tag, TAG_MAP['default'])
            tr_tag = tag_info['tr']
            tag_color = tag_info['color']
            
            word_frame = tk.Frame(results_frame, bd=2, relief="raised", bg=tag_color)
            word_frame.pack(side="left", padx=5, pady=10)
            
            word_label = tk.Label(word_frame, text=word, font=word_font, bg=tag_color, fg="#1c2833")
            word_label.pack(padx=10, pady=(5,0))
            
            tag_label = tk.Label(word_frame, text=tr_tag, font=tag_font, bg=tag_color, fg="#2c3e50")
            tag_label.pack(padx=10, pady=(0,5))

def clear_all():
    entry_sentence.delete(0, tk.END)
    for widget in results_frame.winfo_children():
        widget.destroy()

def load_example_sentence():
    clear_all()
    example = random.choice(EXAMPLE_SENTENCES)
    entry_sentence.insert(0, example)

# --- ARAYÜZ KURULUMU ---
window = tk.Tk()
window.title("Türkçe POS Tagger")
window.geometry("850x550")
window.configure(bg="#2c3e50")

# Fontlar
title_font = font.Font(family="Arial", size=18, weight="bold")
default_font = font.Font(family="Arial", size=12)
word_font = font.Font(family="Arial", size=14, weight="bold")
tag_font = font.Font(family="Arial", size=10)
button_font = font.Font(family="Arial", size=11, weight="bold")

# Ana Çerçeveler
top_frame = tk.Frame(window, bg="#2c3e50")
top_frame.pack(pady=10, padx=20, fill="x")

input_frame = tk.Frame(window, bg="#34495e")
input_frame.pack(pady=10, padx=20, fill="x")

button_frame = tk.Frame(window, bg="#2c3e50")
button_frame.pack(pady=10)

results_frame = tk.Frame(window, bg="#34495e", bd=2, relief="sunken")
results_frame.pack(pady=10, padx=20, fill="both", expand=True)

status_bar = tk.Frame(window, bg="#27ae60", bd=1, relief="sunken")
status_bar.pack(side="bottom", fill="x")

# Arayüz Elemanları
label_title = tk.Label(top_frame, text="Etiketlenecek Cümleyi Girin", font=title_font, bg="#2c3e50", fg="white")
label_title.pack()

entry_sentence = tk.Entry(input_frame, width=80, font=default_font, bd=2, relief="sunken")
entry_sentence.pack(side="left", fill="x", expand=True, ipady=8, padx=5, pady=10)

tag_button = tk.Button(button_frame, text="Etiketle", command=handle_tag_button_click, font=button_font, bg="#27ae60", fg="white", width=15)
tag_button.pack(side="left", padx=5)

example_button = tk.Button(button_frame, text="Örnek Cümle", command=load_example_sentence, font=button_font, bg="#2980b9", fg="white", width=15)
example_button.pack(side="left", padx=5)

clear_button = tk.Button(button_frame, text="Temizle", command=clear_all, font=button_font, bg="#c0392b", fg="white", width=15)
clear_button.pack(side="left", padx=5)

status_var = tk.StringVar()
status_label = tk.Label(status_bar, textvariable=status_var, font=default_font, bg="#27ae60", fg="white")
status_label.pack(pady=3)

# Başlangıçta skoru yükle
load_model_score()
window.mainloop()