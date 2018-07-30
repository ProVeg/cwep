#!/usr/bin/env python
import copy, sys
import tkinter
from tkinter import filedialog
from PyPDF2 import PdfFileWriter, PdfFileReader

root = tkinter.Tk()
root.withdraw()
filez = filedialog.askopenfilenames(parent=root,title='PDFs zum zusammenfügen auswählen',filetypes =(("PDFs", "*.pdf"),("Alle Dateien","*.*")))
sf = filedialog.asksaveasfilename(parent=root,title='Speichern als',defaultextension=".pdf",filetypes =(("PDFs", "*.pdf"),("Alle Dateien","*.*")))
output = PdfFileWriter()
output_page_number = 0
alignment = 2           # to align on even pages
for filename in filez:
    # This code is executed for every file in turn
    input = PdfFileReader(open(filename, 'rb'))
    for p in [input.getPage(i) for i in range(0,input.getNumPages())]:
        # This code is executed for every input page in turn
        output.addPage(p)
        output_page_number += 1
    while output_page_number % alignment != 0:
        output.addBlankPage()
        output_page_number += 1
of = open(sf, 'bw')
output.write(of)
