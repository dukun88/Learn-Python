import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random,string

app = tk.Tk()
app.configure(bg="grey")
app.geometry("400x400")
app.title("Register")

NAMA = tk.StringVar()
EMAIL = tk.StringVar()
USERNAME = tk.StringVar()

frame = ttk.Frame(app)
frame.pack(padx=10,pady=5,fill='x',expand=True)

label1 = ttk.Label(frame, text="Nama Lengkap")
label1.pack(padx=15,pady=8,expand=True,fill='x')
entry1 = ttk.Entry(frame,textvariable=NAMA)
entry1.pack(padx=10,expand=True,fill='x')

label2 = ttk.Label(frame, text="Email")
label2.pack(padx=15,pady=8,expand=True,fill='x')
entry2 = ttk.Entry(frame,textvariable=EMAIL)
entry2.pack(padx=10,expand=True,fill='x')

label3 = ttk.Label(frame, text="Username")
label3.pack(padx=15,pady=8,expand=True,fill='x')
entry3 = ttk.Entry(frame, textvariable=USERNAME)
entry3.pack(padx=10,expand=True,fill='x')

def click():
    randomPass = ''.join((random.choice(string.ascii_letters) for i in range(12)))
    pesan = f"Hello {NAMA.get()}! \n This is your admin Password:\n {randomPass}"
    showinfo(title="WELCOME!",message=pesan)
    


button = ttk.Button(frame, text="Confirm", command=click)
button.pack(padx=15,pady=8,expand=True,fill='x')
app.mainloop()