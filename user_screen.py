import tkinter as tk
import random

random_number = random.randint(1, 101)

value_expectation = "Expectation..."
previous_input = ""  

def on_change_input(event):
    global value_expectation, previous_input  
    input_number = entry.get().strip()  

    if input_number != previous_input:  
        label2.config(fg="red")  
        previous_input = input_number  
    else:
        label2.config(fg="green")  

    input_number = int(input_number or 0)  

    if input_number > random_number:
        value_expectation = "Small Number plz !!!"

    elif input_number < random_number:
        value_expectation = "Greater Number plz !!!"

    else:
        value_expectation = "Congratulations"


    label2.config(text=value_expectation)

    root.after(1000, clear_input)

def clear_input():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Assume number")
root.iconbitmap("think.ico")
root.geometry("600x350")

label = tk.Label(root, text="Enter Number (1-100):", width=30)
label.config(font=("Verdana", 20), fg="blue")
label.pack()

entry = tk.Entry(root, font="20")
entry.pack(padx=10, pady=10, ipady=5)
entry.focus_set()
entry.bind("<KeyRelease>", lambda event: root.after(800, on_change_input, event))

label2 = tk.Label(root, text=value_expectation, width=25)
label2.config(font=("Verdana", 17),fg="gray")
label2.pack()

root.mainloop()
