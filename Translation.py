import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkPDFViewer import tkPDFViewer as pdf
import PyPDF2
from fpdf import FPDF
from libretranslatepy import LibreTranslateAPI
my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window 
my_w.title('Libre Translator')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='Add PDF file to be translated',width=30,font=my_font1)  
l1.grid(row=1,column=1)
b1 = tk.Button(my_w, text='Upload File', 
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1) 

def translate(text, source_lang, language):
    translator = LibreTranslateAPI()
    translated_text = translator.translate(text, source_lang, language)
    print(translated_text)
    return translated_text

def write_pdf(output_path, translated_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    paragraphs = translated_text.split('\n')
    for p in paragraphs:
        pdf.multi_cell(0, 5, p)
        pdf.ln()

    pdf.output(output_path)

def upload_file():
    
    f_types = [('pdf Files', '*.pdf')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    if filename:
        pdf_file=PyPDF2.PdfReader(filename)
        extracted_text = ''

        for pageObj in pdf_file.pages:
            extracted_text += pageObj.extract_text()
        translated_text = translate(extracted_text, "en", "de")    
        write_pdf(output_file, translated_text)


output_file = 'C:/Users/prans/OneDrive/Desktop/Libre/output.pdf'
        

my_w.mainloop()  # Keep the window open
