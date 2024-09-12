import tkinter as tk
import random
import pyperclip as cp

lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
common_symbols = ['!','@','#','$','%','&','*']

class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.prompt = tk.Label(self, text="Password length")
        self.entry = tk.Scale(self, orient="horizontal", length=256, from_=10.0, to=256.0)
        self.symboltext = tk.Label(self, text="Number of symbols (max 100)", anchor="center")
        self.symbolcount = tk.Spinbox(self, from_=1.0, to=100.0)
        self.numbertext = tk.Label(self, text="Number of numbers (max 100)", anchor="center")
        self.numbercount = tk.Spinbox(self, from_=1.0, to=100.0)
        self.submit = tk.Button(self, text="Generate", command = self.calculate)
        self.output = tk.Label(self, text="")
        self.output2 = tk.Label(self, text="")

        # lay the widgets out on the screen. 
        self.prompt.pack(side="top", fill="x", padx=20)
        self.entry.pack(side="top", fill="x", padx=20)
        self.symboltext.pack(side="left", fill="x", padx=20)
        self.symbolcount.pack(side="left", fill="x", padx=20)
        self.numbertext.pack(side="left", fill="x", padx=20)
        self.numbercount.pack(side="left", fill="x", padx=20)
        self.submit.pack(side="right", padx=20)
        self.output.pack(side="bottom", fill="x", expand=True, padx=20)
        self.output2.pack(side="bottom", fill="x", expand=True, padx=20)

    def calculate(self):
        password = []
        symbol_count = 0
        number_count = 0

        for i in range(int(self.entry.get())):
            rnd = random.randrange(0,4)

            if(rnd == 0):
                rnd = random.randrange(0,26)
                password.append(lowercase[rnd])
                continue
            if(rnd == 1):
                rnd = random.randrange(0,26)
                password.append(uppercase[rnd])
                continue
            if(rnd == 2 and (number_count < int(self.numbercount.get()))):
                rnd = random.randrange(0,9)
                password.append(numbers[rnd])
                number_count += 1
                continue
            if(rnd == 3 and (symbol_count < int(self.symbolcount.get()))):
                rnd = random.randrange(0,7)
                password.append(common_symbols[rnd])
                symbol_count += 1
                continue

            rnd = random.randrange(0,2)

            if(rnd == 0):
                rnd = random.randrange(0,26)
                password.append(lowercase[rnd])
                continue
            if(rnd == 1):
                rnd = random.randrange(0,26)
                password.append(uppercase[rnd])
                continue

        password = ''.join(password)
        cp.copy(password)
        self.output.configure(text=password)
        self.output2.configure(text="Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Generator")
    Example(root).pack(fill="both", expand=True)
    root.mainloop()