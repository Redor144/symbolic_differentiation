from symbolic.lexer import lexer
from symbolic.parser import parser
import tkinter as tk

if __name__ == '__main__':

    def calculate():
        expression = input_field.get()
        variable = variable_field.get()
        try:
            parsed_expr = parser.parse(expression)
            derivative = parsed_expr.differentiate(variable).simplify()
            result_label.config(text=f"Pochodna: {derivative}")
        except Exception as e:
            tk.messagebox.showerror("Błąd", f"Błąd podczas obliczeń: {e}")
    root = tk.Tk()
    root.title("Symboliczne Różniczkowanie")

    tk.Label(root, text="Wyrażenie:").pack()
    input_field = tk.Entry(root, width=40)
    input_field.pack()

    tk.Label(root, text="Zmienna:").pack()
    variable_field = tk.Entry(root, width=10)
    variable_field.pack()

    calculate_button = tk.Button(root, text="Oblicz", command=calculate)
    calculate_button.pack()

    result_label = tk.Label(root, text="Pochodna pojawi się tutaj")
    result_label.pack()

    root.mainloop()