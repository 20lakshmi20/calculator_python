import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)
root.config(bg="#e0e0e0")

entry = tk.Entry(root, font=("Comic Sans MS", 22), bd=5, relief="sunken", justify="right")
entry.pack(fill="x", padx=10, pady=10)

def press(key):
    if key == "C":
        entry.delete(0, tk.END)
    elif key == "=":
        try:
            result = eval(entry.get())  
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, key)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for r, row in enumerate(buttons):
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for c, char in enumerate(row):
        b = tk.Button(frame, text=char, font=("Comic Sans MS", 18),
                      bg="#f0f0f0", fg="#333333",
                      activebackground="#d0d0d0", command=lambda ch=char: press(ch))
        b.pack(side="left", expand=True, fill="both", padx=5, pady=5)

root.mainloop()