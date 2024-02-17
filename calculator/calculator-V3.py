import tkinter
import math

class ScientificCalculator:
    def __init__(self, tkobj):
        self.tkobj = tkobj
        self.is_degrees = True
        self.entry = tkinter.Entry(tkobj, font=("Arial", 20), bg="white", fg="black", bd=5, width=20)
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

        self.button_list = [
            "sin", "cos", "tan", "log",
            "(", ")", "C", "π",
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ".", "sqrt", "/",
            "e", "^", "=", "Switch DR"
        ]

        self.create_buttons()

    def create_buttons(self):
        r = 1
        c = 0
        for button_text in self.button_list:
            button = tkinter.Button(self.tkobj, width=5, height=2, bd=2, text=button_text, bg="lightblue", fg="black",
                                    font=("Arial", 12, "bold"), command=lambda button_text=button_text: self.click(button_text))
            button.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
            c += 1
            if c > 5:
                r += 1
                c = 0

    def click(self, button_text):
        current_entry = self.entry.get()
        if button_text == 'C':
            self.entry.delete(0, 'end')
        elif button_text == '=':
            try:
                result = eval(current_entry)
                self.entry.delete(0, 'end')
                self.entry.insert('end', str(result))
            except Exception as e:
                self.entry.delete(0, 'end')
                self.entry.insert('end', "Error")
        elif button_text == 'π':
            self.entry.insert('end', str(math.pi))
        elif button_text == 'e':
            self.entry.insert('end', str(math.e))
        elif button_text == 'sqrt':
            result = math.sqrt(float(current_entry))
            self.entry.delete(0, 'end')
            self.entry.insert('end', str(result))
        elif button_text == '^':
            self.entry.insert('end', '**')
        elif button_text == 'Switch DR':
            self.is_degrees = not self.is_degrees
            self.entry.delete(0, 'end')
            self.entry.insert('end', "Degrees" if self.is_degrees else "Radians")
        elif button_text in ['sin', 'cos', 'tan', 'log']:
            func = getattr(math, button_text)
            result = func(float(current_entry))
            self.entry.delete(0, 'end')
            self.entry.insert('end', str(result))
        else:
            self.entry.insert('end', button_text + '(')

def main():
    tkobj = tkinter.Tk()
    tkobj.title("Scientific Calculator")
    tkobj.geometry("500x600")
    tkobj.config(bg="lightblue")

    calculator = ScientificCalculator(tkobj)

    tkobj.mainloop()

if __name__ == "__main__":
    main()
