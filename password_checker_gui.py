import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password_strength():
    password = entry.get()
    strength = 0
    remarks = []

    # Length
    if len(password) >= 12:
        strength += 2
        remarks.append("✅ Good length (12+ characters)")
    elif len(password) >= 8:
        strength += 1
        remarks.append("⚠️ Moderate length (8-11 characters)")
    else:
        remarks.append("❌ Too short (less than 8 characters)")

    # Uppercase
    if re.search(r'[A-Z]', password):
        strength += 1
        remarks.append("✅ Contains uppercase letter")
    else:
        remarks.append("❌ Missing uppercase letter")

    # Lowercase
    if re.search(r'[a-z]', password):
        strength += 1
        remarks.append("✅ Contains lowercase letter")
    else:
        remarks.append("❌ Missing lowercase letter")

    # Digit
    if re.search(r'[0-9]', password):
        strength += 1
        remarks.append("✅ Contains digit")
    else:
        remarks.append("❌ Missing digit")

    # Special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
        remarks.append("✅ Contains special character")
    else:
        remarks.append("❌ Missing special character")

    # Strength level
    if strength >= 6:
        level = "Very Strong 💪"
        color = "green"
    elif strength >= 4:
        level = "Strong 👍"
        color = "blue"
    elif strength >= 2:
        level = "Weak ⚠️"
        color = "orange"
    else:
        level = "Very Weak ❌"
        color = "red"

    # Display result
    result_label.config(text=f"Password Strength: {level}", fg=color)
    details_text.delete("1.0", tk.END)
    for remark in remarks:
        details_text.insert(tk.END, remark + "\n")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", font=("Arial", 14), width=30)
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=5)

details_text = tk.Text(root, height=10, width=45, font=("Arial", 10))
details_text.pack(pady=5)

root.mainloop()
