import pyiwn
import nltk
from guj_to_eng import *
from eng_to_guj import *

# from hindi_to_eng import *
# from eng_to_hindi import *

nltk.download('words')
from nltk.corpus import words

set_of_eng_words = set(words.words())

# print(list(map(str, pyiwn.Language)))
guj_iwn = pyiwn.IndoWordNet(lang=pyiwn.Language.GUJARATI)
hindi_iwn = pyiwn.IndoWordNet(lang=pyiwn.Language.HINDI)

guj_alp = ['અ', 'આ', 'ઇ', 'ઈ', 'ઉ', 'ઊ', 'ઋ', 'એ', 'ઐ', 'ઓ', 'ઔ', 'ઍ', 'ઑ',
           'ા', 'િ', 'ી', 'ુ', 'ૂ', 'ૃ', 'ે', 'ૈ', 'ો', 'ૌ', 'ૅ', 'ૉ', 'ક', 'ચ', 'ટ', 'ત',
           'પ', 'ખ', 'છ', 'ઠ', 'થ', 'ફ', 'ગ', 'જ', 'ડ', 'દ', 'બ', 'ઘ', 'ઝ', 'ઢ', 'ધ', 'ભ',
           'ઙ', 'ઞ', 'ણ', 'ન', 'મ', 'ય', 'ર', 'લ', 'વ', 'શ', 'ષ', 'સ', 'હ', 'ળ', 'ં']

eng_alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

hindi_alp = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः', 'ऋ',
             'ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॅ', 'े', 'ै', 'ॉ', 'ो', 'ौ', 'ं', 'ः', 'ँ',
             'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ',
             'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
             'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श',
             'ष', 'स', 'ह', 'क्ष', 'त्र', 'ज्ञ']

guj_word = 0
hindi_word = 0
eng_word = 0
guj_script = 0
hindi_script = 0
eng_script = 0


def lang_id(word):
    guj = 0
    eng = 0
    hindi = 0
    flag = 0
    global guj_word
    global hindi_word
    global eng_word
    global guj_script
    global hindi_script
    global eng_script
    # word = (input("Enter value: "))
    # print("Entered word: ", word)
    for letter in list(word):
        for letter2 in guj_alp:
            if letter == letter2:
                guj = 1
                break
        for letter2 in eng_alp:
            if letter == letter2:
                eng = 1
                break
        for letter2 in hindi_alp:
            if letter == letter2:
                hindi = 1
                break

    if guj == 1:
        # print("Script: Gujarati")
        guj_script += 1
        try:
            x = guj_iwn.synsets(word)
            # print(word, ": Gujarati")
            guj_word += 1
        except:
            x = guj_to_eng(word)
            for j in x:
                print("Translated English word: 2", j)
                if j in set_of_eng_words:
                    # print(x, ": English 3")
                    eng_word += 1
            # else:
            #     print("'", word, "'", "word not identified in Gujarati")
    elif eng == 1:
        # print("Script: English")
        eng_script += 1
        if word in set_of_eng_words:
            print(word, ": English")
            eng_word += 1
            flag = 1
        y = eng_to_guj(word)
        print("translate Gujarati word: 6", y)
        for j in y:
            try:
                g = guj_iwn.synsets(j)
                print(j, ": Gujarati")
                guj_word += 1
                flag = 1
                break
            except:
                if j == y[-1]:
                    guj_word += 0
                    # print(word, ": Language is not Gujarati ")
        # x = eng_to_hindi(word)
        # print("translate Hindi word: 9", x)
        # for i in x:
        #     try:
        #         h = hindi_iwn.synsets(i)
        #         print(i, ": Hindi")
        #         hindi_word += 1
        #         flag = 1
        #         break
        #     except:
        #         if i == x[-1]:
        #             hindi_word += 0
        #             # print(word, ": Language is not Hindi 11")
        if flag == 0:
            print("'", word, "'", "word not identified")

    # elif hindi == 1:
    #     # print("Script: Hindi")
    #     hindi_script += 1
    #     try:
    #         x = hindi_iwn.synsets(word)
    #         print(word, ": Hindi")
    #         hindi_word += 1
    #     except:
    #         x = hindi_to_eng(word)
    #         # print("Translated English word: 14", x)
    #         if x in set_of_eng_words:
    #             eng_word += 1
    #             print(x, ": English")
    #         else:
    #             print("'", word, "'", "word not identified")
    else:
        print("Please type only in English, Gujarati or Hindi language.")


# input_sentence = input("Enter sentence: ").split()
# for w in input_sentence:
def finale(i_word):
    lang_id(i_word)
    if guj_script:
        scr = 'Gujarati'
        # print("Script: Gujarati, words: ", guj_script)
    elif eng_script:
        scr = 'English'
        # print("Script: English, words: ", eng_script)
    if eng_word:
        lan = 'English'
        # print("Language: English, words: ", eng_word)
    elif guj_word:
        lan = 'Gujarati'
        # print("Language: Gujarati, words: ", guj_word)
    return scr, lan
# if hindi_script:
#         print("Script: Hindi, words: ", hindi_script)
#
# if hindi_word:
#     print("Language: Hindi, words: ", hindi_word)
