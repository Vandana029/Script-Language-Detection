import tkinter
from main import final

window = tkinter.Tk()
window.title("language identification")

word = tkinter.StringVar()
# creating 1  text label and input labels

tkinter.Label(window, text="Enter word").grid(row=0)  # placed in 0 0
input_word = tkinter.Entry(window, width=40, textvariable=word).grid(row=0, column=1)  # placed in 0 1


# creating function called lang():
def lang():
    w = word.get()
    result = final(w)
    if result['error'] == 0:
        tkinter.Label(window, text='Script: ').grid()
        for i in range(len(result['script'])):
            tkinter.Label(window, text=result['script'][i]).grid()

        tkinter.Label(window, text='\nLanguage (Gujarati): ').grid()
        for i in range(len(result['guj_lan'])):
            tkinter.Label(window, text=result['guj_lan'][i]).grid()

        tkinter.Label(window, text='\nLanguage (Hindi): ').grid()
        for i in range(len(result['hindi_lan'])):
            tkinter.Label(window, text=result['hindi_lan'][i]).grid()

        tkinter.Label(window, text='\nLanguage (English): ').grid()
        for i in range(len(result['eng_lan'])):
            tkinter.Label(window, text=result['eng_lan'][i]).grid()

        tkinter.Label(window, text='\nNot Identified Words: ').grid()
        for i in range(len(result['not_iden'])):
            tkinter.Label(window, text=result['not_iden'][i]).grid()
    else:
        tkinter.Label(window, text="Type in Gujarati, Hindi or English language only.").grid()


# def script():
#     tkinter.Label(window, text="Gujarati Script").grid()


tkinter.Button(window, text="Get language", command=lang).grid(row=0, column=2)
# tkinter.Button(window, text="Get Script", command=script).grid(row=1, column=2)

# label = tkinter.Label(window, text='').grid()
window.mainloop()
