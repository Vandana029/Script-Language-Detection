from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import ttk

root = Tk()
# root.Tk()
root.title("On Screen Keyboard")


def select(value):
    if value == "<-":
        # txt = text.get(1.0, END)
        # val = len(txt)
        # txt.delete(1.0, END)
        # text.insert(1.0, txt[:val - 2])
        txt = text.get(1.0, END)
        val = len(txt)
        text.delete(1.0, END)
        # txt.delete('1.0', END)
        text.insert(1.0, txt[:val - 2])

    elif value == "Space":
        text.insert(END, " ")
    elif value == "Tab":
        text.insert(END, " ")
    else:
        text.insert(END, value)


# app = Tk()
# root.geometry("700x350")


# main = Menu(root)
# edit = Menu(main)
# edit.add_command(label='Gujarati')
# edit.add_command(label="Hindi")
# edit.add_command(label="English")
# root.config(menu=main)
# main.add_cascade(label='Language', menu=edit)

def eng_kb():
    buttons = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
               '<-', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
               'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Space']

    varrow = 2
    varcolumn = 0

    for button in buttons:
        command = lambda x=button: select(x)
        if button != 'Space':
            Button(root, text=button, width=5, bg="Black", fg="white", activebackground="white",
                   activeforeground="black",
                   relief=RIDGE, padx=8, pady=4, bd=6, command=command).grid(row=varrow, column=varcolumn)
        if button == 'Space':
            Button(root, text=button, width=5, bg="Black", fg="white", activebackground="white",
                   activeforeground="black",
                   relief=RIDGE, padx=8, pady=4, bd=6, command=command).grid(row=4, column=7)

        varcolumn += 1
        if varcolumn > 9 and varrow in [2, 3]:
            varcolumn = 0
            varrow += 1
        elif varcolumn > 7 and varrow == 4:
            for i in range(varcolumn, 10):
                Button(root, text='', width=5,
                       padx=8, pady=4, bd=0, relief=FLAT).grid(row=varrow, column=i)
            for i in range(varrow + 1, 9):
                for j in range(10):
                    Button(root, text='', width=5,
                           padx=8, pady=4, bd=0, relief=FLAT).grid(row=i, column=j)
            #     if varcolumn > 9:
            #         varcolumn = 0
            #         break
            # for i in range(varrow + 1, 9):
            #     for j in range(10):
            #         Button(root, text='', width=5,
            #                padx=8, pady=4, bd=0, relief=FLAT).grid(row=varrow, column=varcolumn)


def guj_kb():
    buttons = ['ક', 'ચ', 'ટ', 'ત', 'પ', 'ખ', 'છ', 'ઠ', 'થ', 'ફ',
               'ગ', 'જ', 'ડ', 'દ', 'બ', 'ઘ', 'ઝ', 'ઢ', 'ધ', 'ભ',
               'ઙ', 'ઞ', 'ણ', 'ન', 'મ', 'ય', 'ર', 'લ', 'વ', 'શ',
               'ષ', 'સ', 'હ', 'ળ', 'જ્ઞ', 'અ', 'આ', 'ઇ', 'ઈ', 'ઉ',
               'ઊ', 'ઋ', 'એ', 'ઐ', 'ઓ', 'ઔ', 'ા', 'િ', 'ી', 'ુ',
               'ૂ', 'ૃ', 'ે', 'ૈ', 'ો', 'ૌ', 'ૅ', 'ૉ', 'ં', 'Space',
               '<-']

    varrow = 2
    varcolumn = 0

    for button in buttons:
        command = lambda x=button: select(x)
        if button != 'Space':
            Button(root, text=button, width=5, bg="Black", fg="white", activebackground="white",
                   activeforeground="black",
                   relief=RIDGE, padx=8, pady=4, bd=6, command=command).grid(row=varrow, column=varcolumn)
        if button == 'Space':
            Button(root, text=button, width=5, bg="Black", fg="white", activebackground="white",
                   activeforeground="black",
                   relief=RIDGE, padx=8, pady=4, bd=6, command=command).grid(row=7, column=9)

        varcolumn += 1
        if varcolumn > 9 and varrow in [2, 3, 4, 5, 6, 7]:
            varcolumn = 0
            varrow += 1
        elif varrow == 6 and varcolumn > 8:
            for i in range(varcolumn, 10):
                Button(root, text='', width=5,
                       padx=8, pady=4, bd=0, relief=FLAT).grid(row=varrow, column=i)
            for i in range(varrow + 1, 9):
                for j in range(10):
                    Button(root, text='', width=5,
                           padx=8, pady=4, bd=0, relief=FLAT).grid(row=i, column=j)


def hindi_kb():
    buttons = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ',
               'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
               'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श',
               'ष', 'स', 'ह', 'क्ष', 'त्र', 'ज्ञ', 'अ', 'आ', 'इ', 'ई',
               'उ', 'ऊ', 'ऋ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः', 'ा',
               'ि', 'ी', 'ु', 'ू', 'ृ', 'ॅ', 'े', 'ै', 'ॉ', 'ो',
               'ौ', '्', 'Space', '<-']

    varrow = 2
    varcolumn = 0

    for button in buttons:
        command = lambda x=button: select(x)
        if button != 'Space':
            Button(root, text=button, width=5, bg="Black", fg="white", activebackground="white",
                   activeforeground="black",
                   relief=RIDGE, padx=8, pady=4, bd=6, command=command).grid(row=varrow, column=varcolumn)
        if button == 'Space':
            Button(root, text=button, width=5, bg="Black", fg="white", activebackground="white",
                   activeforeground="black",
                   relief=RIDGE, padx=8, pady=4, bd=6, command=command).grid(row=8, column=2)

        varcolumn += 1
        if varcolumn > 9 and varrow in [2, 3, 4, 5, 6, 7]:
            varcolumn = 0
            varrow += 1
        elif varrow == 8 and varcolumn > 3:
            for i in range(varcolumn, 10):
                Button(root, text='', width=5,
                       padx=8, pady=4, bd=0, relief=FLAT).grid(row=varrow, column=i)
            for i in range(varrow + 1, 9):
                for j in range(10):
                    Button(root, text='', width=5,
                           padx=8, pady=4, bd=0, relief=FLAT).grid(row=i, column=j)


def callback(*arg):
    if cb.current() == 0:
        hindi_kb()
    elif cb.current() == 1:
        eng_kb()
    else:
        guj_kb()


languages = ('Hindi', 'English', 'Gujarati')

# Create a combobox widget
var = StringVar()
cb = ttk.Combobox(root, textvariable=var)
# cb.clipboard_append("het")
# cb = ttk.Combobox(root)
cb['values'] = languages
cb['state'] = 'readonly'
cb.grid(row=0, columnspan=8)

var.trace('w', callback)

text = scrolledtext.ScrolledText(root, width=120, height=5, wrap=WORD, padx=10, pady=10, borderwidth=5, relief=RIDGE)
text.grid(row=1, columnspan=16)

root.mainloop()
