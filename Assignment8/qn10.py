import tkinter as tk

def rupeesToEuro():
    rupees = float(rupees_entry.get())
    euro = rupees * 0.011  
    euro_entry.delete(0, tk.END) 
    euro_entry.insert(tk.END, euro)

def euroToRupees():
    euro = float(euro_entry.get())
    rupees = euro / 0.011  
    rupees_entry.delete(0, tk.END)  
    rupees_entry.insert(tk.END, rupees)

window = tk.Tk()
window.title("Currency Converter")

rupees_label = tk.Label(window, text="Rupees:")
rupees_label.grid(row=0, column=0, padx=5, pady=5)

rupees_entry = tk.Entry(window, width=10)
rupees_entry.insert(tk.END, "0.0")
rupees_entry.grid(row=1, column=0, padx=5, pady=5)

euro_label = tk.Label(window, text="Euro:")
euro_label.grid(row=0, column=1, padx=5, pady=5)

euro_entry = tk.Entry(window, width=10)
euro_entry.insert(tk.END, "0.0")
euro_entry.grid(row=1, column=1, padx=5, pady=5)

rupee_to_euro_button = tk.Button(window, text="R->E", command=rupeesToEuro)
rupee_to_euro_button.grid(row=2, column=0, padx=5, pady=5)

euro_to_rupee_button = tk.Button(window, text="E->R", command=euroToRupees)
euro_to_rupee_button.grid(row=2, column=1, padx=5, pady=5)

# Start the main event loop
window.mainloop()