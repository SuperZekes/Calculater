import tkinter as tk

operators = {
  "+": lambda x, y: x + y,
  "-": lambda x, y: x - y, 
  "*": lambda x, y: x * y,
  "/": lambda x, y: x / y
}

def calculate():
  num1 = int(num1_entry.get())
  num2 = int(num2_entry.get())
  
  operation = operator_var.get()
  result = operators[operation](num1, num2)
  
  result_label.config(text="Your answer is: " + str(result))

root = tk.Tk()
root.title("Calculator")

num1_entry = tk.Entry(root)
num1_entry.pack()

num2_entry = tk.Entry(root)
num2_entry.pack() 

operator_var = tk.StringVar()
operator_var.set("+") 

tk.Radiobutton(root, text="+", variable=operator_var, value="+").pack()
tk.Radiobutton(root, text="-", variable=operator_var, value="-").pack()
tk.Radiobutton(root, text="*", variable=operator_var, value="*").pack()
tk.Radiobutton(root, text="/", variable=operator_var, value="/").pack()

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.geometry("270x243")
root.mainloop()