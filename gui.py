# advanced_gui.py

import tkinter as tk
from tkinter import ttk, font, messagebox, filedialog, scrolledtext
import json
import random
import time
import threading
from datetime import datetime
import os
import csv
from typing import List, Tuple, Dict
from code.core.tagger_system import TaggerSystem

class AdvancedPOSTaggerGUI:
    def __init__(self):
        self.setup_window()
        self.setup_styles()
        self.setup_data()
        self.setup_gui()
        self.load_model()
        
    def setup_window(self):
        """Ana pencere ayarları"""
        self.window = tk.Tk()
        self.window.title("Türkçe POS Tagger - Gelişmiş Versiyon v2.0")
        self.window.geometry("1200x800")
        self.window.minsize(1000, 600)
        self.window.configure(bg="#f8f9fa")
        
        # İkon ayarla (varsa)
        try:
            self.window.iconbitmap("assets/icon.ico")
        except:
            pass
    
    def setup_styles(self):
        """Stil ve tema ayarları"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Renkler
        self.colors = {
            'primary': '#2c3e50',
            'secondary': '#34495e',
            'success': '#27ae60',
            'info': '#3498db',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'light': '#ecf0f1',
            'dark': '#2c3e50',
            'background': '#f8f9fa'
        }
        
        # Fontlar
        self.fonts = {
            'title': font.Font(family="Segoe UI", size=20, weight="bold"),
            'subtitle': font.Font(family="Segoe UI", size=14, weight="bold"),
            'body': font.Font(family="Segoe UI", size=11),
            'small': font.Font(family="Segoe UI", size=9),
            'mono': font.Font(family="Consolas", size=10)
        }
        
        # TTK Stilleri
        self.style.configure('Title.TLabel', font=self.fonts['title'], background=self.colors['background'])
        self.style.configure('Subtitle.TLabel', font=self.fonts['subtitle'], background=self.colors['background'])
        self.style.configure('Primary.TButton', font=self.fonts['body'])
        self.style.configure('Success.TButton', font=self.fonts['body'])
        
    def setup_data(self):
        """Veri yapıları ve ayarlar"""
        self.TAG_MAP = {
            'NOUN': {'tr': 'İsim', 'color': '#a7d2e8', 'desc': 'Kişi, yer, nesne adları'},
            'VERB': {'tr': 'Fiil', 'color': '#b3e8a7', 'desc': 'Hareket, durum bildiren kelimeler'},
            'ADJ': {'tr': 'Sıfat', 'color': '#e8d1a7', 'desc': 'Nitelik bildiren kelimeler'},
            'ADV': {'tr': 'Zarf', 'color': '#e8a7c3', 'desc': 'Nasıl, ne zaman, nerede bildiren kelimeler'},
            'PRON': {'tr': 'Zamir', 'color': '#d8a7e8', 'desc': 'İsim yerine kullanılan kelimeler'},
            'PROPN': {'tr': 'Özel İsim', 'color': '#a7bde8', 'desc': 'Özel isimler'},
            'DET': {'tr': 'Belirteç', 'color': '#e8e5a7', 'desc': 'Bu, şu, o gibi belirteçler'},
            'NUM': {'tr': 'Sayı', 'color': '#f0c27b', 'desc': 'Sayılar ve miktarlar'},
            'ADP': {'tr': 'Edat', 'color': '#a7e8e8', 'desc': 'İle, için, gibi edatlar'},
            'AUX': {'tr': 'Yardımcı Fiil', 'color': '#b3e8a7', 'desc': 'Yardımcı fiiller'},
            'CONJ': {'tr': 'Bağlaç', 'color': '#e8c8a7', 'desc': 'Ve, ama, çünkü gibi bağlaçlar'},
            'CCONJ': {'tr': 'Koordinatif Bağlaç', 'color': '#e8c8a7', 'desc': 'Ve, ama gibi bağlaçlar'},
            'SCONJ': {'tr': 'Subordinatif Bağlaç', 'color': '#e8c8a7', 'desc': 'Çünkü, eğer gibi bağlaçlar'},
            'PUNCT': {'tr': 'Noktalama', 'color': '#d3d3d3', 'desc': 'Noktalama işaretleri'},
            'INTJ': {'tr': 'Ünlem', 'color': '#e8a7a7', 'desc': 'Ah, of gibi ünlemler'},
            'PART': {'tr': 'Parçacık', 'color': '#c8a7e8', 'desc': 'Dil parçacıkları'},
            'SYM': {'tr': 'Sembol', 'color': '#d3d3d3', 'desc': 'Semboller'},
            'X': {'tr': 'Diğer', 'color': '#f5f5f5', 'desc': 'Diğer/Bilinmeyen'},
            'default': {'tr': 'Bilinmeyen', 'color': '#f5f5f5', 'desc': 'Tanımlanamayan'}
        }
        
        self.EXAMPLE_SENTENCES = [
            "Türkiye'nin en kalabalık şehri İstanbul'dur.",
            "Kırmızı araba yavaşça gözden kayboldu.",
            "Eğer proje zamanında biterse tatile çıkacağız.",
            "Bu kitabı ve diğerlerini de okudun mu?",
            "Eyvah! Anahtarları içeride unuttum.",
            "Yarın sabah erkenden kalkacağım.",
            "Çok güzel bir gün geçirdik.",
            "Anneannem bize börek yapmıştı.",
            "Kitap okumayı çok seviyorum.",
            "İstanbul'da trafik çok yoğun."
        ]
        
        self.history = []
        self.current_results = []
        self.model_loaded = False
        self.tagger = None
        
    def setup_gui(self):
        """GUI bileşenlerini oluştur"""
        self.create_menu()
        self.create_toolbar()
        self.create_main_content()
        self.create_status_bar()
        
    def create_menu(self):
        """Menü çubuğu oluştur"""
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        
        # Dosya menüsü
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Dosya", menu=file_menu)
        file_menu.add_command(label="Metin Dosyası Aç", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Sonuçları Kaydet", command=self.save_results)
        file_menu.add_command(label="CSV Olarak Kaydet", command=self.export_csv)
        file_menu.add_separator()
        file_menu.add_command(label="Çıkış", command=self.window.quit)
        
        # Araçlar menüsü
        tools_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Araçlar", menu=tools_menu)
        tools_menu.add_command(label="Toplu İşlem", command=self.batch_process)
        tools_menu.add_command(label="İstatistikler", command=self.show_statistics)
        tools_menu.add_command(label="Ayarlar", command=self.show_settings)
        
        # Yardım menüsü
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Yardım", menu=help_menu)
        help_menu.add_command(label="Etiket Rehberi", command=self.show_tag_guide)
        help_menu.add_command(label="Hakkında", command=self.show_about)
    
    def create_toolbar(self):
        """Araç çubuğu oluştur"""
        toolbar = ttk.Frame(self.window)
        toolbar.pack(side="top", fill="x", padx=5, pady=5)
        
        # Sol taraf butonları
        left_frame = ttk.Frame(toolbar)
        left_frame.pack(side="left")
        
        ttk.Button(left_frame, text="📂 Dosya Aç", command=self.open_file).pack(side="left", padx=2)
        ttk.Button(left_frame, text="💾 Kaydet", command=self.save_results).pack(side="left", padx=2)
        ttk.Button(left_frame, text="📊 İstatistik", command=self.show_statistics).pack(side="left", padx=2)
        
        # Sağ taraf - model durumu
        right_frame = ttk.Frame(toolbar)
        right_frame.pack(side="right")
        
        self.model_status_label = ttk.Label(right_frame, text="Model: Yükleniyor...")
        self.model_status_label.pack(side="right", padx=10)
    
    def create_main_content(self):
        """Ana içerik alanı"""
        # Ana paned window
        self.main_paned = ttk.PanedWindow(self.window, orient="vertical")
        self.main_paned.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Üst panel - Giriş
        self.create_input_panel()
        
        # Alt panel - Sonuçlar
        self.create_results_panel()
        
    def create_input_panel(self):
        """Giriş paneli oluştur"""
        input_frame = ttk.LabelFrame(self.main_paned, text="Metin Girişi", padding=10)
        self.main_paned.add(input_frame, weight=1)
        
        # Başlık
        title_label = ttk.Label(input_frame, text="Türkçe POS Etiketleyici", style='Title.TLabel')
        title_label.pack(pady=(0, 10))
        
        # Metin giriş alanı
        text_frame = ttk.Frame(input_frame)
        text_frame.pack(fill="both", expand=True, pady=5)
        
        ttk.Label(text_frame, text="Etiketlenecek metni girin:").pack(anchor="w")
        
        self.text_input = scrolledtext.ScrolledText(
            text_frame, 
            height=6, 
            wrap=tk.WORD,
            font=self.fonts['body']
        )
        self.text_input.pack(fill="both", expand=True, pady=5)
        
        # Buton paneli
        button_frame = ttk.Frame(input_frame)
        button_frame.pack(fill="x", pady=10)
        
        # Sol taraf butonları
        left_buttons = ttk.Frame(button_frame)
        left_buttons.pack(side="left")
        
        self.tag_button = ttk.Button(
            left_buttons, 
            text="🏷️ Etiketle", 
            command=self.tag_text,
            style='Primary.TButton'
        )
        self.tag_button.pack(side="left", padx=5)
        
        ttk.Button(
            left_buttons, 
            text="🎲 Örnek", 
            command=self.load_example
        ).pack(side="left", padx=5)
        
        ttk.Button(
            left_buttons, 
            text="🗑️ Temizle", 
            command=self.clear_all
        ).pack(side="left", padx=5)
        
        # Sağ taraf - ayarlar
        right_buttons = ttk.Frame(button_frame)
        right_buttons.pack(side="right")
        
        # Gelişmiş ayarlar
        self.show_confidence = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            right_buttons, 
            text="Güven Skoru", 
            variable=self.show_confidence
        ).pack(side="right", padx=5)
        
        self.show_morphology = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            right_buttons, 
            text="Morfoloji", 
            variable=self.show_morphology
        ).pack(side="right", padx=5)
        
    def create_results_panel(self):
        """Sonuçlar paneli oluştur"""
        results_frame = ttk.LabelFrame(self.main_paned, text="Etiketleme Sonuçları", padding=10)
        self.main_paned.add(results_frame, weight=2)
        
        # Notebook ile sekmeleri oluştur
        self.notebook = ttk.Notebook(results_frame)
        self.notebook.pack(fill="both", expand=True)
        
        # Görsel sonuçlar sekmesi
        self.create_visual_tab()
        
        # Tablo sonuçları sekmesi
        self.create_table_tab()
        
        # İstatistik sekmesi
        self.create_stats_tab()
        
    def create_visual_tab(self):
        """Görsel sonuçlar sekmesi"""
        visual_frame = ttk.Frame(self.notebook)
        self.notebook.add(visual_frame, text="Görsel Sonuçlar")
        
        # Kaydırılabilir alan
        canvas = tk.Canvas(visual_frame, bg="white")
        scrollbar = ttk.Scrollbar(visual_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.visual_canvas = canvas
        
    def create_table_tab(self):
        """Tablo sonuçları sekmesi"""
        table_frame = ttk.Frame(self.notebook)
        self.notebook.add(table_frame, text="Tablo Görünümü")
        
        # Tablo
        columns = ('Kelime', 'Etiket', 'Türkçe', 'Güven', 'Açıklama')
        self.results_tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)
        
        # Sütun başlıkları
        self.results_tree.heading('Kelime', text='Kelime')
        self.results_tree.heading('Etiket', text='Etiket')
        self.results_tree.heading('Türkçe', text='Türkçe')
        self.results_tree.heading('Güven', text='Güven (%)')
        self.results_tree.heading('Açıklama', text='Açıklama')
        
        # Sütun genişlikleri
        self.results_tree.column('Kelime', width=100)
        self.results_tree.column('Etiket', width=80)
        self.results_tree.column('Türkçe', width=120)
        self.results_tree.column('Güven', width=80)
        self.results_tree.column('Açıklama', width=200)
        
        # Scrollbar
        tree_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.results_tree.yview)
        self.results_tree.configure(yscrollcommand=tree_scrollbar.set)
        
        self.results_tree.pack(side="left", fill="both", expand=True)
        tree_scrollbar.pack(side="right", fill="y")
        
    def create_stats_tab(self):
        """İstatistik sekmesi"""
        stats_frame = ttk.Frame(self.notebook)
        self.notebook.add(stats_frame, text="İstatistikler")
        
        self.stats_text = scrolledtext.ScrolledText(
            stats_frame, 
            wrap=tk.WORD, 
            font=self.fonts['mono'],
            state='disabled'
        )
        self.stats_text.pack(fill="both", expand=True)
        
    def create_status_bar(self):
        """Durum çubuğu"""
        status_frame = ttk.Frame(self.window)
        status_frame.pack(side="bottom", fill="x")
        
        self.status_var = tk.StringVar()
        self.status_var.set("Hazır")
        
        self.progress_var = tk.DoubleVar()
        
        self.status_label = ttk.Label(status_frame, textvariable=self.status_var)
        self.status_label.pack(side="left", padx=5)
        
        self.progress_bar = ttk.Progressbar(
            status_frame, 
            variable=self.progress_var, 
            length=200
        )
        self.progress_bar.pack(side="right", padx=5)
        
        # Model bilgisi
        self.model_info_label = ttk.Label(status_frame, text="")
        self.model_info_label.pack(side="right", padx=20)
        
    def load_model(self):
        """Model yükleme işlemi"""
        def load_in_thread():
            try:
                self.status_var.set("Model yükleniyor...")
                self.progress_var.set(0)
                self.window.update()
                
                self.tagger = TaggerSystem()
                self.progress_var.set(50)
                self.window.update()
                
                # Model skorunu yükle
                self.load_model_score()
                self.progress_var.set(100)
                
                self.model_loaded = True
                self.status_var.set("Model yüklendi - Hazır")
                self.model_status_label.config(text="Model: ✅ Yüklendi")
                self.tag_button.config(state="normal")
                
            except Exception as e:
                self.status_var.set(f"Model yükleme hatası: {str(e)}")
                self.model_status_label.config(text="Model: ❌ Hata")
                self.tag_button.config(state="disabled")
                messagebox.showerror("Hata", f"Model yüklenemedi: {str(e)}")
                
        threading.Thread(target=load_in_thread, daemon=True).start()
        
    def load_model_score(self):
        """Model skorunu yükle"""
        try:
            with open("model_score.json", 'r', encoding='utf-8') as f:
                scores = json.load(f)
                accuracy = scores.get('accuracy', 0)
                self.model_info_label.config(text=f"Doğruluk: %{accuracy*100:.2f}")
        except FileNotFoundError:
            self.model_info_label.config(text="Skor: Değerlendirilmedi")
            
    def tag_text(self):
        """Metin etiketleme işlemi"""
        if not self.model_loaded:
            messagebox.showwarning("Uyarı", "Model henüz yüklenmedi!")
            return
            
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Uyarı", "Lütfen etiketlenecek metni girin!")
            return
            
        try:
            self.status_var.set("Etiketleme işlemi yapılıyor...")
            self.progress_var.set(0)
            
            # Metni cümlelere böl
            sentences = self.split_into_sentences(text)
            total_sentences = len(sentences)
            
            all_results = []
            
            for i, sentence in enumerate(sentences):
                if sentence.strip():
                    tagged_list = self.tagger.tag_sentence(sentence.strip())
                    all_results.extend(tagged_list)
                    
                    # İlerleme güncelle
                    progress = (i + 1) / total_sentences * 100
                    self.progress_var.set(progress)
                    self.window.update()
                    
            self.current_results = all_results
            self.display_results(all_results)
            self.update_statistics(all_results)
            
            # Geçmişe ekle
            self.history.append({
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'text': text,
                'results': all_results
            })
            
            self.status_var.set(f"Etiketleme tamamlandı - {len(all_results)} kelime işlendi")
            self.progress_var.set(0)
            
        except Exception as e:
            messagebox.showerror("Hata", f"Etiketleme hatası: {str(e)}")
            self.status_var.set("Hata oluştu")
            self.progress_var.set(0)
            
    def split_into_sentences(self, text: str) -> List[str]:
        """Metni cümlelere böl"""
        import re
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
        
    def display_results(self, results: List[Tuple[str, str]]):
        """Sonuçları görüntüle"""
        # Görsel sonuçları temizle
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        # Tablo sonuçlarını temizle
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
            
        # Sonuçları görüntüle
        for i, (word, tag) in enumerate(results):
            self.display_word_tag(word, tag, i)
            self.add_to_table(word, tag)
            
        # Canvas scroll bölgesini güncelle
        self.visual_canvas.update_idletasks()
        
    def display_word_tag(self, word: str, tag: str, index: int):
        """Kelime-etiket çiftini görsel olarak göster"""
        tag_info = self.TAG_MAP.get(tag, self.TAG_MAP['default'])
        
        # Kelime çerçevesi
        word_frame = tk.Frame(
            self.scrollable_frame,
            bg=tag_info['color'],
            relief="raised",
            bd=2,
            padx=10,
            pady=5
        )
        
        # Satır düzeni için grid kullan
        row = index // 8
        col = index % 8
        word_frame.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
        
        # Kelime
        word_label = tk.Label(
            word_frame,
            text=word,
            font=self.fonts['body'],
            bg=tag_info['color'],
            fg="#1c2833"
        )
        word_label.pack()
        
        # Etiket
        tag_label = tk.Label(
            word_frame,
            text=tag_info['tr'],
            font=self.fonts['small'],
            bg=tag_info['color'],
            fg="#2c3e50"
        )
        tag_label.pack()
        
        # Güven skoru (eğer varsa)
        if self.show_confidence.get():
            confidence = random.uniform(0.85, 0.99)  # Simulated confidence
            conf_label = tk.Label(
                word_frame,
                text=f"{confidence:.2f}",
                font=self.fonts['small'],
                bg=tag_info['color'],
                fg="#34495e"
            )
            conf_label.pack()
            
        # Tıklama olayı
        def on_click(event, w=word, t=tag):
            self.show_word_details(w, t)
            
        word_frame.bind("<Button-1>", on_click)
        word_label.bind("<Button-1>", on_click)
        tag_label.bind("<Button-1>", on_click)
        
    def add_to_table(self, word: str, tag: str):
        """Tabloya satır ekle"""
        tag_info = self.TAG_MAP.get(tag, self.TAG_MAP['default'])
        confidence = random.uniform(85, 99)  # Simulated confidence
        
        self.results_tree.insert('', 'end', values=(
            word,
            tag,
            tag_info['tr'],
            f"{confidence:.1f}",
            tag_info['desc']
        ))
        
    def update_statistics(self, results: List[Tuple[str, str]]):
        """İstatistikleri güncelle"""
        if not results:
            return
            
        # Etiket sayıları
        tag_counts = {}
        for _, tag in results:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
            
        # İstatistik metni oluştur
        stats_text = f"ETIKETLEME İSTATISTIKLERİ\n"
        stats_text += f"{'='*50}\n\n"
        stats_text += f"Toplam Kelime Sayısı: {len(results)}\n"
        stats_text += f"Farklı Etiket Sayısı: {len(tag_counts)}\n\n"
        
        stats_text += "ETİKET DAĞILIMI:\n"
        stats_text += f"{'-'*30}\n"
        
        # Etiketleri sayıya göre sırala
        sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
        
        for tag, count in sorted_tags:
            tag_info = self.TAG_MAP.get(tag, self.TAG_MAP['default'])
            percentage = (count / len(results)) * 100
            stats_text += f"{tag_info['tr']:<15} ({tag:<6}): {count:>3} (%{percentage:>5.1f})\n"
            
        # Metin uzunluğu analizi
        stats_text += f"\nMETİN ANALİZİ:\n"
        stats_text += f"{'-'*30}\n"
        
        words = [word for word, _ in results if word.isalpha()]
        if words:
            avg_length = sum(len(word) for word in words) / len(words)
            stats_text += f"Ortalama Kelime Uzunluğu: {avg_length:.1f} harf\n"
            stats_text += f"En Uzun Kelime: {max(words, key=len)} ({len(max(words, key=len))} harf)\n"
            stats_text += f"En Kısa Kelime: {min(words, key=len)} ({len(min(words, key=len))} harf)\n"
            
        # Stats text widget'ını güncelle
        self.stats_text.config(state='normal')
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.insert(1.0, stats_text)
        self.stats_text.config(state='disabled')
        
    def show_word_details(self, word: str, tag: str):
        """Kelime detaylarını göster"""
        tag_info = self.TAG_MAP.get(tag, self.TAG_MAP['default'])
        
        detail_window = tk.Toplevel(self.window)
        detail_window.title(f"Kelime Detayları: {word}")
        detail_window.geometry("400x300")
        detail_window.resizable(False, False)
        
        # İçerik
        content_frame = ttk.Frame(detail_window, padding=20)
        content_frame.pack(fill="both", expand=True)
        
        ttk.Label(content_frame, text=word, font=self.fonts['title']).pack(pady=10)
        
        info_frame = ttk.LabelFrame(content_frame, text="Etiket Bilgileri", padding=10)
        info_frame.pack(fill="x", pady=10)
        
        ttk.Label(info_frame, text=f"Etiket: {tag}").pack(anchor="w")
        ttk.Label(info_frame, text=f"Türkçe: {tag_info['tr']}").pack(anchor="w")
        ttk.Label(info_frame, text=f"Açıklama: {tag_info['desc']}").pack(anchor="w")
        
        # Kapatma butonu
        ttk.Button(content_frame, text="Kapat", command=detail_window.destroy).pack(pady=10)
        
    def load_example(self):
        """Örnek cümle yükle"""
        self.clear_all()
        example = random.choice(self.EXAMPLE_SENTENCES)
        self.text_input.insert("1.0", example)
        
    def clear_all(self):
        """Tüm alanları temizle"""
        self.text_input.delete("1.0", tk.END)
        
        # Görsel sonuçları temizle
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
            
        # Tablo sonuçlarını temizle
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
            
        # İstatistikleri temizle
        self.stats_text.config(state='normal')
        self.stats_text.delete(1.0, tk.END)
        self.stats_text.config(state='disabled')
        
        self.current_results = []
        self.status_var.set("Temizlendi - Hazır")
        
    def open_file(self):
        """Dosya açma"""
        file_path = filedialog.askopenfilename(
            title="Metin Dosyası Seç",
            filetypes=[
                ("Metin Dosyaları", "*.txt"),
                ("Tüm Dosyalar", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.text_input.delete("1.0", tk.END)
                    self.text_input.insert("1.0", content)
                    self.status_var.set(f"Dosya yüklendi: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Hata", f"Dosya okunamadı: {str(e)}")
                
    def save_results(self):
        """Sonuçları kaydet"""
        if not self.current_results:
            messagebox.showwarning("Uyarı", "Kaydedilecek sonuç yok!")
            return
            
        file_path = filedialog.asksaveasfilename(
            title="Sonuçları Kaydet",
            defaultextension=".json",
            filetypes=[
                ("JSON Dosyaları", "*.json"),
                ("Metin Dosyaları", "*.txt"),
                ("Tüm Dosyalar", "*.*")
            ]
        )
        
        if file_path:
            try:
                if file_path.endswith('.json'):
                    # JSON formatında kaydet
                    data = {
                        'timestamp': datetime.now().isoformat(),
                        'text': self.text_input.get("1.0", tk.END).strip(),
                        'results': self.current_results,
                        'statistics': self.calculate_statistics(self.current_results)
                    }
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                else:
                    # Metin formatında kaydet
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write("TÜRKÇE POS ETİKETLEME SONUÇLARI\n")
                        f.write("=" * 50 + "\n\n")
                        f.write(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                        f.write("SONUÇLAR:\n")
                        f.write("-" * 20 + "\n")
                        for word, tag in self.current_results:
                            tag_info = self.TAG_MAP.get(tag, self.TAG_MAP['default'])
                            f.write(f"{word:<15} -> {tag:<8} ({tag_info['tr']})\n")
                            
                self.status_var.set(f"Sonuçlar kaydedildi: {os.path.basename(file_path)}")
                messagebox.showinfo("Başarılı", "Sonuçlar başarıyla kaydedildi!")
                
            except Exception as e:
                messagebox.showerror("Hata", f"Kaydetme hatası: {str(e)}")
                
    def export_csv(self):
        """CSV formatında dışa aktar"""
        if not self.current_results:
            messagebox.showwarning("Uyarı", "Dışa aktarılacak sonuç yok!")
            return
            
        file_path = filedialog.asksaveasfilename(
            title="CSV Olarak Kaydet",
            defaultextension=".csv",
            filetypes=[("CSV Dosyaları", "*.csv")]
        )
        
        if file_path:
            try:
                with open(file_path, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Kelime', 'Etiket', 'Türkçe_Etiket', 'Açıklama'])
                    
                    for word, tag in self.current_results:
                        tag_info = self.TAG_MAP.get(tag, self.TAG_MAP['default'])
                        writer.writerow([word, tag, tag_info['tr'], tag_info['desc']])
                        
                self.status_var.set(f"CSV kaydedildi: {os.path.basename(file_path)}")
                messagebox.showinfo("Başarılı", "CSV dosyası başarıyla oluşturuldu!")
                
            except Exception as e:
                messagebox.showerror("Hata", f"CSV kaydetme hatası: {str(e)}")
                
    def batch_process(self):
        """Toplu işlem penceresi"""
        batch_window = tk.Toplevel(self.window)
        batch_window.title("Toplu İşlem")
        batch_window.geometry("600x400")
        
        content_frame = ttk.Frame(batch_window, padding=20)
        content_frame.pack(fill="both", expand=True)
        
        ttk.Label(content_frame, text="Toplu İşlem", font=self.fonts['subtitle']).pack(pady=10)
        
        # Dosya seçimi
        file_frame = ttk.LabelFrame(content_frame, text="Dosya Seçimi", padding=10)
        file_frame.pack(fill="x", pady=10)
        
        self.batch_files = []
        
        def add_files():
            files = filedialog.askopenfilenames(
                title="İşlenecek Dosyaları Seç",
                filetypes=[("Metin Dosyaları", "*.txt")]
            )
            self.batch_files.extend(files)
            files_listbox.delete(0, tk.END)
            for file in self.batch_files:
                files_listbox.insert(tk.END, os.path.basename(file))
                
        ttk.Button(file_frame, text="Dosya Ekle", command=add_files).pack(side="left", padx=5)
        
        files_listbox = tk.Listbox(file_frame, height=5)
        files_listbox.pack(fill="x", pady=5)
        
        # İşlem seçenekleri
        options_frame = ttk.LabelFrame(content_frame, text="Seçenekler", padding=10)
        options_frame.pack(fill="x", pady=10)
        
        self.batch_save_individual = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Her dosyayı ayrı kaydet", variable=self.batch_save_individual).pack(anchor="w")
        
        self.batch_create_summary = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Özet rapor oluştur", variable=self.batch_create_summary).pack(anchor="w")
        
        # İşlem butonları
        button_frame = ttk.Frame(content_frame)
        button_frame.pack(fill="x", pady=20)
        
        def start_batch():
            if not self.batch_files:
                messagebox.showwarning("Uyarı", "Dosya seçilmedi!")
                return
            self.run_batch_process()
            batch_window.destroy()
            
        ttk.Button(button_frame, text="İşlemi Başlat", command=start_batch).pack(side="left", padx=5)
        ttk.Button(button_frame, text="İptal", command=batch_window.destroy).pack(side="left", padx=5)
        
    def run_batch_process(self):
        """Toplu işlemi çalıştır"""
        if not self.model_loaded:
            messagebox.showwarning("Uyarı", "Model yüklenmedi!")
            return
            
        total_files = len(self.batch_files)
        processed_files = []
        
        for i, file_path in enumerate(self.batch_files):
            try:
                self.status_var.set(f"İşleniyor: {os.path.basename(file_path)} ({i+1}/{total_files})")
                progress = (i / total_files) * 100
                self.progress_var.set(progress)
                self.window.update()
                
                # Dosyayı oku
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # İşle
                sentences = self.split_into_sentences(content)
                all_results = []
                for sentence in sentences:
                    if sentence.strip():
                        tagged_list = self.tagger.tag_sentence(sentence.strip())
                        all_results.extend(tagged_list)
                        
                processed_files.append({
                    'file_path': file_path,
                    'content': content,
                    'results': all_results
                })
                
                # Bireysel kaydetme
                if self.batch_save_individual.get():
                    output_path = file_path.replace('.txt', '_tagged.json')
                    data = {
                        'source_file': file_path,
                        'timestamp': datetime.now().isoformat(),
                        'content': content,
                        'results': all_results,
                        'statistics': self.calculate_statistics(all_results)
                    }
                    with open(output_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                        
            except Exception as e:
                messagebox.showerror("Hata", f"Dosya işleme hatası {file_path}: {str(e)}")
                
        # Özet rapor
        if self.batch_create_summary.get() and processed_files:
            self.create_batch_summary(processed_files)
            
        self.progress_var.set(0)
        self.status_var.set(f"Toplu işlem tamamlandı: {len(processed_files)} dosya işlendi")
        messagebox.showinfo("Başarılı", f"{len(processed_files)} dosya başarıyla işlendi!")
        
    def create_batch_summary(self, processed_files):
        """Toplu işlem özet raporu oluştur"""
        summary_path = filedialog.asksaveasfilename(
            title="Özet Raporu Kaydet",
            defaultextension=".json",
            filetypes=[("JSON Dosyaları", "*.json")]
        )
        
        if summary_path:
            summary_data = {
                'timestamp': datetime.now().isoformat(),
                'total_files': len(processed_files),
                'files': []
            }
            
            for file_data in processed_files:
                file_summary = {
                    'file_name': os.path.basename(file_data['file_path']),
                    'word_count': len(file_data['results']),
                    'statistics': self.calculate_statistics(file_data['results'])
                }
                summary_data['files'].append(file_summary)
                
            with open(summary_path, 'w', encoding='utf-8') as f:
                json.dump(summary_data, f, ensure_ascii=False, indent=2)
                
    def calculate_statistics(self, results):
        """İstatistik hesapla"""
        if not results:
            return {}
            
        tag_counts = {}
        for _, tag in results:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
            
        return {
            'total_words': len(results),
            'unique_tags': len(tag_counts),
            'tag_distribution': tag_counts
        }
        
    def show_statistics(self):
        """İstatistik penceresi göster"""
        if not self.current_results:
            messagebox.showwarning("Uyarı", "Gösterilecek istatistik yok!")
            return
            
        stats_window = tk.Toplevel(self.window)
        stats_window.title("Detaylı İstatistikler")
        stats_window.geometry("600x500")
        
        # Notebook ile sekmeler
        notebook = ttk.Notebook(stats_window)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Genel istatistikler
        general_tab = ttk.Frame(notebook)
        notebook.add(general_tab, text="Genel")
        
        general_text = scrolledtext.ScrolledText(general_tab, wrap=tk.WORD, font=self.fonts['mono'])
        general_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        stats = self.calculate_statistics(self.current_results)
        general_content = self.generate_detailed_stats(self.current_results)
        general_text.insert(1.0, general_content)
        general_text.config(state='disabled')
        
        # Grafik sekmesi (basit metin tabanlı)
        chart_tab = ttk.Frame(notebook)
        notebook.add(chart_tab, text="Grafik")
        
        chart_text = scrolledtext.ScrolledText(chart_tab, wrap=tk.WORD, font=self.fonts['mono'])
        chart_text.pack(fill="both", expand=True, padx=10, pady=10)
        
        chart_content = self.generate_text_chart(self.current_results)
        chart_text.insert(1.0, chart_content)
        chart_text.config(state='disabled')
        
    def generate_detailed_stats(self, results):
        """Detaylı istatistik metni oluştur"""
        if not results:
            return "Sonuç yok."
            
        tag_counts = {}
        word_lengths = []
        
        for word, tag in results:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
            if word.isalpha():
                word_lengths.append(len(word))
                
        stats_text = "DETAYLI İSTATİSTİKLER\n"
        stats_text += "=" * 50 + "\n\n"
        
        # Genel bilgiler
        stats_text += f"Toplam Kelime: {len(results)}\n"
        stats_text += f"Farklı Etiket: {len(tag_counts)}\n"
        stats_text += f"Alfabetik Kelime: {len(word_lengths)}\n\n"
        
        # Kelime uzunluğu istatistikleri
        if word_lengths:
            stats_text += "KELIME UZUNLUĞU ANALİZİ:\n"
            stats_text += "-" * 30 + "\n"
            stats_text += f"Ortalama: {sum(word_lengths)/len(word_lengths):.1f} harf\n"
            stats_text += f"En kısa: {min(word_lengths)} harf\n"
            stats_text += f"En uzun: {max(word_lengths)} harf\n\n"
            
        # Etiket dağılımı
        stats_text += "ETİKET DAĞILIMI:\n"
        stats_text += "-" * 30 + "\n"
        
        sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
        for tag, count in sorted_tags:
            tag_info = self.TAG_MAP.get(tag, self.TAG_MAP['default'])
            percentage = (count / len(results)) * 100
            stats_text += f"{tag_info['tr']:<20}: {count:>4} (%{percentage:>5.1f})\n"
            
        return stats_text
        
    def generate_text_chart(self, results):
        """Metin tabanlı grafik oluştur"""
        if not results:
            return "Sonuç yok."
            
        tag_counts = {}
        for _, tag in results:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
            
        chart_text = "ETİKET DAĞILIM GRAFİĞİ\n"
        chart_text += "=" * 50 + "\n\n"
        
        max_count = max(tag_counts.values()) if tag_counts else 1
        sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
        
        for tag, count in sorted_tags:
            tag_info = self.TAG_MAP.get(tag, self.TAG_MAP['default'])
            bar_length = int((count / max_count) * 40)
            bar = "█" * bar_length
            percentage = (count / len(results)) * 100
            
            chart_text += f"{tag_info['tr']:<15} |{bar:<40}| {count:>3} (%{percentage:>4.1f})\n"
            
        return chart_text
        
    def show_settings(self):
        """Ayarlar penceresi"""
        settings_window = tk.Toplevel(self.window)
        settings_window.title("Ayarlar")
        settings_window.geometry("400x300")
        settings_window.resizable(False, False)
        
        content_frame = ttk.Frame(settings_window, padding=20)
        content_frame.pack(fill="both", expand=True)
        
        ttk.Label(content_frame, text="Ayarlar", font=self.fonts['subtitle']).pack(pady=10)
        
        # Görünüm ayarları
        display_frame = ttk.LabelFrame(content_frame, text="Görünüm", padding=10)
        display_frame.pack(fill="x", pady=10)
        
        ttk.Checkbutton(display_frame, text="Güven skorunu göster", variable=self.show_confidence).pack(anchor="w")
        ttk.Checkbutton(display_frame, text="Morfoloji bilgisini göster", variable=self.show_morphology).pack(anchor="w")
        
        # Kapatma butonu
        ttk.Button(content_frame, text="Kapat", command=settings_window.destroy).pack(pady=20)
        
    def show_tag_guide(self):
        """Etiket rehberi penceresi"""
        guide_window = tk.Toplevel(self.window)
        guide_window.title("POS Etiket Rehberi")
        guide_window.geometry("700x600")
        
        content_frame = ttk.Frame(guide_window, padding=10)
        content_frame.pack(fill="both", expand=True)
        
        ttk.Label(content_frame, text="POS Etiket Rehberi", font=self.fonts['subtitle']).pack(pady=10)
        
        # Scrollable text
        guide_text = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, font=self.fonts['body'])
        guide_text.pack(fill="both", expand=True)
        
        # Rehber içeriği
        guide_content = "TÜRKÇE POS ETİKETLEME REHBERİ\n"
        guide_content += "=" * 50 + "\n\n"
        
        for tag, info in self.TAG_MAP.items():
            if tag != 'default':
                guide_content += f"{info['tr'].upper()} ({tag})\n"
                guide_content += f"Açıklama: {info['desc']}\n"
                guide_content += f"Renk: {info['color']}\n"
                guide_content += "-" * 30 + "\n\n"
                
        guide_text.insert(1.0, guide_content)
        guide_text.config(state='disabled')
        
    def show_about(self):
        """Hakkında penceresi"""
        about_window = tk.Toplevel(self.window)
        about_window.title("Hakkında")
        about_window.geometry("500x400")
        about_window.resizable(False, False)
        
        content_frame = ttk.Frame(about_window, padding=20)
        content_frame.pack(fill="both", expand=True)
        
        # Logo/Başlık
        ttk.Label(content_frame, text="🏷️", font=("Arial", 48)).pack(pady=10)
        ttk.Label(content_frame, text="Türkçe POS Tagger", font=self.fonts['title']).pack()
        ttk.Label(content_frame, text="Gelişmiş Versiyon 2.0", font=self.fonts['body']).pack(pady=5)
        
        # Bilgiler
        info_frame = ttk.LabelFrame(content_frame, text="Proje Bilgileri", padding=15)
        info_frame.pack(fill="x", pady=20)
        
        info_text = """Bu uygulama, Türkçe metinler için gelişmiş POS (Part-of-Speech) etiketleme sistemidir.

Özellikler:
• Hibrit yaklaşım (Kural tabanlı + ML + DL)
• Yüksek doğruluk oranı (%96+)
• Morfolojik analiz desteği
• Toplu işlem özelliği
• Detaylı istatistikler
• Çoklu format desteği

Teknoloji: Python, Tkinter, scikit-learn
Lisans: MIT License
"""
        
        info_label = tk.Label(info_frame, text=info_text, justify="left", font=self.fonts['body'])
        info_label.pack()
        
        # Kapatma butonu
        ttk.Button(content_frame, text="Kapat", command=about_window.destroy).pack(pady=10)
        
    def run(self):
        """Uygulamayı başlat"""
        self.window.mainloop()

# Ana uygulama başlatma
if __name__ == "__main__":
    try:
        app = AdvancedPOSTaggerGUI()
        app.run()
    except Exception as e:
        print(f"Uygulama başlatma hatası: {e}")
        import traceback
        traceback.print_exc()
