# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter as tk


root = tk.Tk()

root.geometry("500x500")
root.title("my first GUI")


label = tk.Label(root, text ="Master mind" , font =('Arial',20))
label.pack(padx=20 , pady=20)

textbox = tk.Text(root, height=3 , font =('Arial',20))
textbox.pack(padx=10 , pady=10)

button = tk.Button(root, text="click me", font =('Arial', 18))
button.pack(padx=10, pady=10)

root.mainloop()


