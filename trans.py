import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    input_text = input_entry.get("1.0", "end-1c")
    source_lang = source_language_combo.get()
    target_lang = target_language_combo.get()
    
    translator = Translator()
    translated = translator.translate(input_text, src=source_lang, dest=target_lang)
    
    output_text.delete("1.0", "end")
    output_text.insert("1.0", translated.text)

def create_label(text, parent):
    label = tk.Label(parent, text=text)
    label.pack()

def create_combobox(values, parent, default):
    combo = ttk.Combobox(parent, values=values, state="readonly")
    combo.set(default)
    combo.pack()
    return combo

# Create the main window
window = tk.Tk()
window.title("Language Translation App")

# Create and arrange widgets
create_label("Enter text to translate:", window)
input_entry = tk.Text(window, width=40, height=5)
input_entry.pack()

create_label("Select source and target languages:", window)

languages = ['auto', 'en', 'es', 'fr', 'de', 'it', 'ja', 'ko', 'pt', 'zh']
source_language_combo = create_combobox(languages, window, "auto")
target_language_combo = create_combobox(languages, window, "en")

translate_button = tk.Button(window, text="Translate", command=translate_text)
translate_button.pack()

create_label("Translation:", window)
output_text = tk.Text(window, width=40, height=5)
output_text.pack()

# Start the main loop
window.mainloop()