#python -m venv .venv
#.venv\Scripts\activate.bat

import tkinter as tk
import text_analyzer

def run(): 
    text_analyzer.TextAnalyser(file_name='text.txt', pos_list=['VERB', 'NOUN'])

window = tk.Tk()
label = tk.Label(window, text="Анализатор текста", font=("Impact", 19))
button = tk.Button(window, font=("Impact", 17), background="#DAA520", text="сделать вордклауд", command=run)
label.pack()
button.pack()
entry = tk.Entry()
entry.pack
float(entry.get())






window.mainloop()