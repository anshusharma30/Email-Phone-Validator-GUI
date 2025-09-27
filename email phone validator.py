import re
import tkinter as tk
from tkinter import messagebox

# ---------- Validation Functions ----------
def validate_email():
    email = entry_email.get()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        messagebox.showinfo("Result", f"✅ Valid Email: {email}")
    else:
        messagebox.showerror("Result", f"❌ Invalid Email: {email}")

def validate_phone():
    phone = entry_phone.get()
    pattern = r'^(\+91|0)?[6-9]\d{9}$'
    if re.match(pattern, phone):
        messagebox.showinfo("Result", f"✅ Valid Phone Number: {phone}")
    else:
        messagebox.showerror("Result", f"❌ Invalid Phone Number: {phone}")

# ---------- Tkinter GUI ----------
root = tk.Tk()
root.title("Email & Phone Validator")
root.geometry("400x250")
root.resizable(False, False)

# Title Label
label_title = tk.Label(root, text="📧 Email & 📱 Phone Validator", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

# Email Section
frame_email = tk.Frame(root)
frame_email.pack(pady=5)
tk.Label(frame_email, text="Enter Email:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
entry_email = tk.Entry(frame_email, width=30)
entry_email.grid(row=0, column=1, padx=5)
btn_email = tk.Button(frame_email, text="Validate Email", command=validate_email)
btn_email.grid(row=0, column=2, padx=5)

# Phone Section
frame_phone = tk.Frame(root)
frame_phone.pack(pady=5)
tk.Label(frame_phone, text="Enter Phone:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
entry_phone = tk.Entry(frame_phone, width=30)
entry_phone.grid(row=0, column=1, padx=5)
btn_phone = tk.Button(frame_phone, text="Validate Phone", command=validate_phone)
btn_phone.grid(row=0, column=2, padx=5)

# Exit Button
btn_exit = tk.Button(root, text="Exit", width=10, command=root.quit, bg="red", fg="white")
btn_exit.pack(pady=15)

root.mainloop()
