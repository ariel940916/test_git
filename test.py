import tkinter as tk
from tkinter import messagebox

# ----- 進位轉換實做（核心演算法） -----

# 十進位轉N進位 (n=2或16)
def dec_to_baseN(n, base):
    if n == 0:
        return '0'
    digits = []
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    while n > 0:
        remainder = n % base
        if remainder >= 10:
            digits.append(chr(ord('A') + remainder - 10))
        else:
            digits.append(str(remainder))
        n //= base
    if is_negative:
        digits.append('-')
    return ''.join(digits[::-1])

def dec_to_bin(n):
    return dec_to_baseN(n, 2)

def dec_to_hex(n):
    return dec_to_baseN(n, 16)

# N進位轉十進位 (base=2 or 16)
def baseN_to_dec(s, base):
    s = s.strip().upper()
    if not s:
        raise ValueError("Empty input")
    if s[0] == '-':
        sign = -1
        s = s[1:]
    else:
        sign = 1
    n = 0
    for c in s:
        if '0' <= c <= '9':
            val = ord(c) - ord('0')
        elif 'A' <= c <= 'F':
            val = ord(c) - ord('A') + 10
        else:
            raise ValueError(f"Invalid character {c} for base {base}")
        if val >= base:
            raise ValueError(f"Digit {c} not valid for base {base}")
        n = n * base + val
    return sign * n

def bin_to_dec(s):
    return baseN_to_dec(s, 2)

def hex_to_dec(s):
    return baseN_to_dec(s, 16)

# 輸入有效性檢查
def validate_bin(s):
    s = s.strip()
    if not s:
        raise ValueError("Empty input")
    if s[0] == '-':
        body = s[1:]
    else:
        body = s
    if any(c not in '01' for c in body):
        raise ValueError("Binary should consist of 0,1 only")
    return True

def validate_hex(s):
    s = s.strip().upper()
    if not s:
        raise ValueError("Empty input")
    if s[0] == '-':
        body = s[1:]
    else:
        body = s
    for c in body:
        if not (('0' <= c <= '9') or ('A' <= c <= 'F')):
            raise ValueError("Invalid hex digit")
    return True

def validate_dec(s):
    s = s.strip()
    if not s:
        raise ValueError("Empty input")
    if s[0] == '-':
        body = s[1:]
    else:
        body = s
    if not body.isdigit():
        raise ValueError("Decimal should be number only")
    return True

# ----- GUI 設定 -----

def convert(event=None):
    try:
        if bin_var.get().strip():
            # 用 binary 為基準
            validate_bin(bin_var.get())
            d = bin_to_dec(bin_var.get())
            dec_var.set(str(d))
            hex_var.set(dec_to_hex(d))
        elif dec_var.get().strip():
            # 用 decimal 為基準
            validate_dec(dec_var.get())
            d = int(dec_var.get())
            bin_var.set(dec_to_bin(d))
            hex_var.set(dec_to_hex(d))
        elif hex_var.get().strip():
            # 用 hex 為基準
            validate_hex(hex_var.get())
            d = hex_to_dec(hex_var.get())
            dec_var.set(str(d))
            bin_var.set(dec_to_bin(d))
        else:
            messagebox.showwarning("警告", "請輸入一欄數值！")
    except Exception as e:
        messagebox.showerror("錯誤", f"轉換錯誤： {e}")

def clear_all():
    bin_var.set("")
    dec_var.set("")
    hex_var.set("")

root = tk.Tk()
root.title("進位轉換器 (2, 10, 16) by Copilot")

tk.Label(root, text="二進位 (Bin)").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="十進位 (Dec)").grid(row=1, column=0, padx=5, pady=5)
tk.Label(root, text="十六進位 (Hex)").grid(row=2, column=0, padx=5, pady=5)

bin_var = tk.StringVar()
dec_var = tk.StringVar()
hex_var = tk.StringVar()

bin_entry = tk.Entry(root, textvariable=bin_var, width=25)
dec_entry = tk.Entry(root, textvariable=dec_var, width=25)
hex_entry = tk.Entry(root, textvariable=hex_var, width=25)
bin_entry.grid(row=0, column=1, padx=5)
dec_entry.grid(row=1, column=1, padx=5)
hex_entry.grid(row=2, column=1, padx=5)

convert_btn = tk.Button(root, text="轉換", command=convert, width=8)
convert_btn.grid(row=3, column=0, pady=10)

clear_btn = tk.Button(root, text="清除", command=clear_all, width=8)
clear_btn.grid(row=3, column=1, pady=10)

root.bind('<Return>', convert)  # 按 Enter 也可以轉換

root.mainloop()
 
