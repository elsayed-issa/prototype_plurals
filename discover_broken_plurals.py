import json
from tkinter import *
import tkinter.messagebox
from difflib import get_close_matches

class IPA_Converter:

    def __init__(self):
        self.dictionary_1 = {}
        self.dictionary_2 = {}
        self.ipa_dictionary()

    def ipa_dictionary(self):
        self.dictionary_1 = {
            u"\u0627": "A",  # ا
            u"\u0628": "b",  # ب
            u"\u062A": 't', # ت
            u"\u062B": 'v', # ث
            u"\u062C": 'j', # ج
            u"\u062D": 'H', # ح
            u"\u062E": 'x', # خ
            u"\u062F": 'd', # د
            u"\u0630": '*', # ذ
            u"\u0631": 'r', # ر
            u"\u0632": 'z', # ز
            u"\u0633": 's', # س
            u"\u0634": '$', # ش
            u"\u0635": 'S', # ص
            u"\u0636": 'D', # ض
            u"\u0637": 'T', # ط
            u"\u0638": 'Z', # ظ
            u"\u0639": 'E', # ع
            u"\u063A": 'g', # غ
            u"\u0641": 'f', # ف
            u"\u0642": 'q', # ق
            u"\u0643": 'k', # ك
            u"\u0644": 'l', # ل
            u"\u0645": 'm', # م
            u"\u0646": 'n', # ن
            u"\u0647": 'h', # هـ
            u"\u0648": 'w', # و
            u"\u0649": 'y', # ى
            u"\u064A": 'y',  # ي  
            u"\u0629": 'p',  #  ة
            # hamzas
            #u"\u0621": '\',
            u"\u0623": '>',
            u"\u0625": '<',
            u"\u0624": '&',
            u"\u0626": '}',
            #u"\u0654": '\', # Hamza above
            #u"\u0655": '\',
            u"\u0622": '|',
            # diacritics
            u"\u064E": 'a',
            u"\u064F": 'u',
            u"\u0650": 'i',
            u"\u0651": '~',
            u"\u0652": 'o',
            u"\u064B": 'F',
            u"\u064C": 'N',
            u"\u064D": 'K',
        }
        self.dictionary_2 = {
            "A": u"\u0627",  # ا
            "b": u"\u0628",  # ب
            't': u"\u062A",  # ت
            'v': u"\u062B",  # ث
            'j': u"\u062C",  # ج
            'H': u"\u062D",  # ح
            'x': u"\u062E",  # خ
            'd': u"\u062F",  # د
            '*': u"\u0630",  # ذ
            'r': u"\u0631",  # ر
            'z': u"\u0632",  # ز
            's': u"\u0633",  # س
            '$': u"\u0634",  # ش
            'S': u"\u0635",  # ص
            'D': u"\u0636",  # ض
            'T': u"\u0637",  # ط
            'Z': u"\u0638",  # ظ
            'E': u"\u0639",  # ع
            'g': u"\u063A",  # غ
            'f': u"\u0641",  # ف
            'q': u"\u0642",  # ق
            'k': u"\u0643",  # ك
            'l': u"\u0644",  # ل
            'm': u"\u0645",  # م
            'n': u"\u0646",  # ن
            'h': u"\u0647",  # هـ
            'w': u"\u0648",  # و
            'y': u"\u0649",  # ى
            'y': u"\u064A",  # ي
            'p': u"\u0629",  # ة
            # hamzas
            #u"\u0621": '\',
            '>': u"\u0623",
            '<': u"\u0625",
            '&': u"\u0624",
            '}': u"\u0626",
            #u"\u0654": '\', # Hamza above
            #u"\u0655": '\',
            '|': u"\u0622",
            # diacritics
            'a': u"\u064E",
            'u': u"\u064F",
            'i': u"\u0650",
            '~': u"\u0651",
            'o': u"\u0652",
            'F': u"\u064B",
            'N': u"\u064C",
            'K': u"\u064D",
        }

    def ara_2_buck(self, text):
        # create empty string to which we append the results of the loop
        transcribed_text = u''
        # replace every character with its sound in the above dictionary 
        for i in range(len(text)): # loop the indexes of the string
            if text[i] in self.dictionary_1: # find every index in the dictionary above
                transcribed_text += self.dictionary_1[text[i]]  # map it to the corresponding ipa symbol
        return transcribed_text

    def buck_2_ara(self, text):
        # create empty string to which we append the results of the loop
        transcribed_text = u''
        # replace every character with its sound in the above dictionary
        for i in range(len(text)):  # loop the indexes of the string
            if text[i] in self.dictionary_2:  # find every index in the dictionary above
                # map it to the corresponding ipa symbol
                transcribed_text += self.dictionary_2[text[i]]
        return transcribed_text


data = json.load(open("data.json"))

def translate(w):
    # converts to lower case
    #w = w.lower()
    if w in data:
        return data[w]
    # for getting close matches of word
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean % s instead? Enter Y if yes, or N if no: " %
                   get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


class IPA_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title('Find Arabic Broken Plurals')
        self.root.geometry('600x600')
        
        #--------------- Functions ------------#
        def find(text):
            found_text = text
            found_text = ipa.ara_2_buck(found_text)
            found_text = translate(found_text)
            d = {ipa.buck_2_ara(key) : ipa.buck_2_ara(val) for (key,val) in found_text.items()}
            return ("\n".join("{!r}: {!r}".format(k, v) for k, v in d.items()))

                
        def transcribe():
            myOutput.delete(0.0, END)
            if myInput.get(0.0, END) != '':
                result = find(myInput.get(0.0, END))
                myOutput.insert(INSERT, result)
            else:
                myOutput.insert(INSERT, 'Please enter some text here!!')
            
        def quit():
            quit = tkinter.messagebox.askyesno(
                'Find Arabic Broken Plurals', 'Would you like to quit?')
            if quit > 0:
                return exit()

        def clear():
            myInput.delete('1.0', END)
            myOutput.delete('1.0', END)

        #--------------- Title ---------------#
        title = Label(self.root, text='Find Arabic Broken Plurals')
        title.pack(side=TOP, fill=X)

        #--------------- Frame ----------------#
        topFrame = LabelFrame(self.root, bd = 2, relief=RIDGE, bg='light grey')
        topFrame.place(x=20, y=30, width=560, height=420)

        btn_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='light grey')
        btn_Frame.place(x=20, y=465, width=560, height=100)

        #-------------- Buttons ----------------#
        self.searchbutton = Button(btn_Frame, text='Find', command=transcribe, width=10, height=2).grid(
            row=0, column=0, padx=40, pady=30)
        self.clearbutton = Button(btn_Frame, text='Clear', command=clear, width=10,height=2).grid(row=0, column=1, padx=40, pady=30)
        self.quitbutton = Button(btn_Frame, text='Quit', command=quit ,width=10,height=2).grid(row=0, column=2, padx=40, pady=30)

        #-------------- Label and Entry ----------------#
        myLabel_1 = Label(topFrame, text='Enter the plural pattern',bg='light grey')
        myLabel_1.pack()

        myInput = Text(topFrame, width=75, height=2)
        myInput.configure(font=("Times New Roman", 16, "bold"))
        myInput.pack()

        myLabel_2 = Label(topFrame, text='Results',bg='light grey')
        myLabel_2.pack()

        myOutput = Text(topFrame, width=75, height=20)
        myOutput.configure(font=("Times New Roman", 20, "bold"))
        myOutput.pack()

        #-----------------------------------------------#
   
if __name__ == '__main__':
    root = Tk()
    root.resizable(width=False, height=False)
    myApp = IPA_GUI(root)
    ipa = IPA_Converter()
    translate = translate
    root.mainloop()


