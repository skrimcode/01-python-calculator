import tkinter as tk
from tkinter import messagebox

class SkrimCalc:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.configure(bg='#2C3E50')
        self.root.geometry("320x450")
        
        self.current_text = ""
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.setup_ui()
    
    def setup_ui(self):
        display_frame = tk.Frame(self.root, bg='#2C3E50')
        display_frame.pack(pady=15)
        
        display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=('Arial', 18),
            justify='right',
            bd=0,
            bg='#34495E',
            fg='white',
            readonlybackground='#34495E'
        )
        display.pack(padx=10, ipady=8)
        display.config(state='readonly')
        
        button_frame = tk.Frame(self.root, bg='#2C3E50')
        button_frame.pack(pady=5)
        
        button_layout = [
            ['C', '±', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '=']
        ]
        
        for r, row_buttons in enumerate(button_layout):
            for c, btn_text in enumerate(row_buttons):
                if btn_text:
                    self.make_button(button_frame, btn_text, r, c)
    
    def make_button(self, parent, text, row, col):
        if text in ['/', '*', '-', '+', '=']:
            color = '#E67E22'
            text_color = 'white'
        elif text in ['C', '±', '%']:
            color = '#95A5A6'
            text_color = 'black'
        else:
            color = '#34495E'
            text_color = 'white'
        
        if text == '0':
            btn = tk.Button(
                parent,
                text=text,
                font=('Arial', 14),
                bg=color,
                fg=text_color,
                bd=0,
                command=lambda: self.process_input(text)
            )
            btn.grid(row=row, column=col, columnspan=2, sticky='ew', padx=1, pady=1, ipadx=18)
        else:
            btn = tk.Button(
                parent,
                text=text,
                font=('Arial', 14),
                bg=color,
                fg=text_color,
                bd=0,
                command=lambda: self.process_input(text)
            )
            btn.grid(row=row, column=col, sticky='ew', padx=1, pady=1, ipadx=18)
        
        parent.grid_columnconfigure(col, weight=1)
    
    def process_input(self, key):
        try:
            if key == 'C':
                self.current_text = ""
                self.display_var.set("0")
            
            elif key == '±':
                if self.current_text and self.current_text != "0":
                    if self.current_text[0] == '-':
                        self.current_text = self.current_text[1:]
                    else:
                        self.current_text = '-' + self.current_text
                    self.display_var.set(self.current_text)
            
            elif key == '%':
                if self.current_text:
                    num_val = float(self.current_text) / 100
                    self.current_text = str(num_val)
                    self.display_var.set(self.current_text)
            
            elif key == '=':
                calc_result = eval(self.current_text.replace('×', '*').replace('÷', '/'))
                self.current_text = str(calc_result)
                self.display_var.set(self.current_text)
            
            elif key in ['+', '-', '*', '/']:
                if self.current_text and self.current_text[-1] not in ['+', '-', '*', '/']:
                    self.current_text += key
                    self.display_var.set(self.current_text)
            
            elif key == '.':
                if not self.current_text:
                    self.current_text = "0."
                elif '.' not in self.current_text.split()[-1]:
                    self.current_text += key
                self.display_var.set(self.current_text)
            
            else:
                if self.current_text == "0":
                    self.current_text = key
                else:
                    self.current_text += key
                self.display_var.set(self.current_text)
                
        except:
            messagebox.showerror("Error", "Invalid calculation")
            self.current_text = ""
            self.display_var.set("0")
    
    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SkrimCalc()
    app.start()
