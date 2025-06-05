import qrcode
import tkinter as tk
from tkinter import filedialog

def generate_qr():
    url = entry.get()
    if not url:
        return
    
    qr = qrcode.make(url)
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if file_path:
        qr.save(file_path)
        status_label.config(text=f"QR save: {file_path}")

root = tk.Tk()
root.title("QR Code Generator")

tk.Label(root, text="Your link:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

generate_btn = tk.Button(root, text="Create QR", command=generate_qr)
generate_btn.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
