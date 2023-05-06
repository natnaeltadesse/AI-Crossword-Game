import tkinter as tk


class RomanToDecimal:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Roman to Decimal Converter")

        # Set up the GUI
        self.label = tk.Label(self.parent, text="Enter a Roman numeral:")
        self.label.pack()

        self.entry = tk.Entry(self.parent)
        self.entry.pack()

        self.convert_button = tk.Button(self.parent, text="Convert", command=self.convert)
        self.convert_button.pack()

        self.result_label = tk.Label(self.parent, text="")
        self.result_label.pack()

    def convert(self):
        roman_numeral = self.entry.get()
        decimal = self.roman_to_decimal(roman_numeral)
        self.result_label.config(text=f"{roman_numeral} is {decimal}")

    def roman_to_decimal(self, roman_numeral):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        decimal = 0
        for i in range(len(roman_numeral)):
            if i > 0 and roman_dict[roman_numeral[i]] > roman_dict[roman_numeral[i - 1]]:
                decimal += roman_dict[roman_numeral[i]] - 2 * roman_dict[roman_numeral[i - 1]]
            else:
                decimal += roman_dict[roman_numeral[i]]
        return decimal


root = tk.Tk()
converter = RomanToDecimal(root)
root.mainloop()
