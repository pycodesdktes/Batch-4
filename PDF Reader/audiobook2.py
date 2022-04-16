from tkinter import *
import PyPDF2
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import filedialog,Canvas,Frame,BOTH,NW
#from PIL import Image ,imageTk
import pyttsx3

root =Tk()
root.title('Praresh-PDF Reader!')
root.geometry("500x500")


# for textbox
my_text= Text(root,height=40,width=70)
my_text.pack(pady=10)

#for clear the textbox
def clear_text_box():
    my_text.delete(1.0,END)
# for open
def open_pdf():
    open_file = filedialog.askopenfilename(
        title="Open PDF file",
        filetypes=(
            ("PDF Files", "*.pdf"),
            ("All Files","*.*")))
    if open_file:
        # for open pdf file
        pdf_file = PyPDF2.PdfFileReader(open_file)
        # for Set the page
        page = pdf_file.getPage(0)
        # exract the text from text from th pdf file
        page_stuff = page.extractText()

        # add text to textbox
        my_text.insert(1.0,page_stuff)


def speak_pdf():
    open_file = filedialog.askopenfilename(
        title="Open PDF file",
        filetypes=(
            ("PDF Files", "*.pdf"),
            ("All Files", "*.*")))
    if open_file:
        # for open pdf file
        pdf_file = PyPDF2.PdfFileReader(open_file)
        # for Set the page
        page = pdf_file.getPage(0)
        # exract the text from text from th pdf file
        page_stuff = page.extractText()

        # add text to textbox
        my_text.insert(1.0, page_stuff)
    speak = pyttsx3.init()
    speak.say(page_stuff)
    speak.runAndWait()



#for menu
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu= Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="Open",command=open_pdf)
file_menu.add_command(label="Clear",command=clear_text_box)
file_menu.add_command(label="listen",command=speak_pdf)

file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)


root.mainloop()