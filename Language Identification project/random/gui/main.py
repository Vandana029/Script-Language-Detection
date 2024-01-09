import pyiwn
import nltk

from gui.eng_to_hindi import *
from gui.eng_to_guj import eng_to_guj
from gui.guj_to_eng import guj_to_eng
from gui.hindi_to_eng import *

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

pron_guj = ['એક્સ્ટ્રા', 'બૅન્ડ', 'અબૅસમન્ટ', 'આય્', 'હર્નિઆ', 'રેસ્પિરેશન', 'ઑલ્વેઝ']

guj_word = 0
hindi_word = 0
eng_word = 0
guj_script = 0
hindi_script = 0
eng_script = 0
result = {'script': [], 'guj_lan': [], 'eng_lan': [], 'hindi_lan': [], 'not_iden': [], 'error': 0}


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
    global result
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
        result['script'].append("Gujarati")
        # print("Script: Gujarati")
        guj_script += 1
        if word in pron_guj:
            result['eng_lan'].append(word)
        else:
            try:
                guj_iwn.synsets(word)
                print(word, ": Gujarati")
                result['guj_lan'].append(word)
                guj_word += 1
            except:
                x = guj_to_eng(word)
                # print("Translated English word: 2", x)
                abc = 0
                for j in x:
                    if j in set_of_eng_words:
                        # print(x, ": English 3")
                        result['eng_lan'].append(word)
                        result['eng_lan'].append('= ' + x)
                        eng_word += 1
                        abc = 1
                if abc == 0:
                    print("'", word, "'", "word not identified in Gujarati")
                    result['not_iden'].append(word)
    elif eng == 1:
        result['script'].append("English")
        # print("Script: English")
        eng_script += 1
        if word in set_of_eng_words:
            print(word, ": English")
            result['eng_lan'].append(word)
            eng_word += 1
            flag = 1
        y = eng_to_guj(word)
        print("translate Gujarati word: 6", y)
        for j in y:
            try:
                g = guj_iwn.synsets(j)
                print(j, ": Gujarati")
                result['guj_lan'].append(word)
                result['guj_lan'].append('= ' + j)
                guj_word += 1
                flag = 1
            except:
                if j == y[-1]:
                    guj_word += 0
                    # print(word, ": Language is not Gujarati ")
        x = eng_to_hindi(word)
        print("translate Hindi word: 9", x)
        for i in x:
            try:
                h = hindi_iwn.synsets(i)
                print(i, ": Hindi")
                result['hindi_lan'].append(word)
                result['hindi_lan'].append('= ' + i)
                hindi_word += 1
                flag = 1
            except:
                if i == x[-1]:
                    hindi_word += 0
                    # print(word, ": Language is not Hindi 11")
        if flag == 0:
            print("'", word, "'", "word not identified")
            result['not_iden'].append(word)
    elif hindi == 1:
        result['script'].append("Hindi")
        # print("Script: Hindi")
        hindi_script += 1
        try:
            x = hindi_iwn.synsets(word)
            print(word, ": Hindi")
            result['hindi_lan'].append(word)
            hindi_word += 1
        except:
            x = hindi_to_eng(word)
            # print("Translated English word: 14", x)
            if x in set_of_eng_words:
                eng_word += 1
                result['eng_lan'].append(word)
                result['eng_lan'].append('= ' + x)
                print(x, ": English")
            else:
                print("'", word, "'", "word not identified")
                result['not_iden'].append(word)
    else:
        print("Please type only in English, Gujarati or Hindi language.")
        result['error'] = 1


def final(sentence):
    input_sentence = sentence.split()
    for w in input_sentence:
        lang_id(w)
    return result
# if guj_script:
#     print("Script: Gujarati, words: ", guj_script)
# if eng_script:
#     print("Script: English, words: ", eng_script)
# if hindi_script:
#     print("Script: Hindi, words: ", hindi_script)
# if guj_word:
#     print("Language: Gujarati, words: ", guj_word)
# if eng_word:
#     print("Language: English, words: ", eng_word)
# if hindi_word:
#     print("Language: Hindi, words: ", hindi_word)
