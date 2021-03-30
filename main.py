import tkinter as tk
import hemming
import checkSum

window = tk.Tk()

window.rowconfigure([0,1,2], minsize=20, weight=1)
window.columnconfigure([0, 1, 2], minsize=20, weight=1)
window.title("Menu principal")
window.geometry("500x500")



b_hamming = tk.Button(master=window, text="Hamming",width=50, command=hemming.start, bg="grey")
b_hamming.grid(row=1,column=1) 

b_checkSum = tk.Button(master= window, text="CheckSum", width=50, command=checkSum.start, bg="grey")
b_checkSum.grid(row=2, column=1)

l_titulo = tk.Label(master=window, text="COMUNICAÇÃO DIGITAL")
l_titulo.grid(row=0,column=1)


window.mainloop()