#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
import tkinter as tk
from tkinter import messagebox

def calculate_difference():
    try:
        # گرفتن سن از کادرهای متن
        son_age = int(entry_son.get())
        father_age = int(entry_father.get())
        
        # محاسبه اختلاف سن
        diff = father_age - son_age
        
        # نمایش نتیجه در یک پنجره کوچک پیام
        messagebox.showinfo("نتیجه", f"Different between your ages: {diff}")
    except ValueError:
        # نمایش خطا در صورت وارد کردن متن به جای عدد
        messagebox.showerror("خطا", "لطفاً عدد وارد کنید!")

# ساخت پنجره اصلی برنامه
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x200")

# برچسب و کادر ورود سن فرزند
label_son = tk.Label(root, text=":سن فرزند را وارد کنید")
label_son.pack(pady=5)
entry_son = tk.Entry(root)
entry_son.pack(pady=5)

# برچسب و کادر ورود سن پدر
label_father = tk.Label(root, text=":سن پدر را وارد کنید")
label_father.pack(pady=5)
entry_father = tk.Entry(root)
entry_father.pack(pady=5)

# دکمه محاسبه
btn_calc = tk.Button(root, text="محاسبه اختلاف سن", command=calculate_difference)
btn_calc.pack(pady=15)

# اجرای برنامه
root.mainloop()
