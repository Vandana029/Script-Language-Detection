#from inltk.inltk import identify_language

guj_alp = ['અ', 'આ', 'ઇ', 'ઈ', 'ઉ', 'ઊ', 'ઋ', 'એ', 'ઐ', 'ઓ', 'ઔ', 'ઍ', 'ઑ',
           'ા', 'િ', 'ી', 'ુ', 'ૂ', 'ૃ', 'ે', 'ૈ', 'ો', 'ૌ', 'ૅ', 'ૉ', 'ક', 'ચ', 'ટ', 'ત',
           'પ', 'ખ', 'છ', 'ઠ', 'થ', 'ફ', 'ગ', 'જ', 'ડ', 'દ', 'બ', 'ઘ', 'ઝ', 'ઢ', 'ધ', 'ભ',
           'ઙ', 'ઞ', 'ણ', 'ન', 'મ', 'ય', 'ર', 'લ', 'વ', 'શ', 'ષ', 'સ', 'હ', 'ળ', 'ં']

eng_alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

guj = 0
eng = 0
gword = 0
eword = 0

sentence = list(input("Enter multiple value: ").split())
for word in sentence:
    for letter in list(word):
        for letter2 in guj_alp:
            if letter == letter2:
                guj = 1
                break
        for letter2 in eng_alp:
            if letter == letter2:
                eng = 1
                break
        if guj == 1:
            gword += 1
            guj = 0
            break
        elif eng == 1:
            eword += 1
            eng = 0
            break
        else:
            print("Please type in English or Gujarati language only.")

if gword != 0 and eword == 0:
    print("Script: Gujarati", "\n", "No of words: ", gword)
elif eword != 0 and gword == 0:
    print("Script: English", "\n", "No of words: ", eword)
elif eword != 0 and gword != 0:
    print("Language: Code Mix (Gujarati + English)", "\n",
          "No of Gujarati words: ", gword, "\n",
          "No of English words: ", eword)




