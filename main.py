import pyiwn
import nltk
from guj_to_eng import *
from eng_to_guj import *
from hindi_to_eng import *
from eng_to_hindi import *

nltk.download('words')
from nltk.corpus import words
set_of_eng_words = set(words.words())

print(list(map(str, pyiwn.Language)))
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
             'ट', 'ठ',	'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न',
             'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श',
             'ष', 'स', 'ह', 'क्ष', 'त्र', 'ज्ञ']

guj = 0
eng = 0
hindi = 0

word = (input("Enter value: "))
print("Entered word: ", word)
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
    print("Script: Gujarati")
    try:
        x = guj_iwn.synsets(word)
        print("Language: Gujarati")
    except:
        x = guj_to_eng(word)
        print("Translated English word: ", x)
        if x in set_of_eng_words:
            print("Language: English")
        else:
            print("word not identified.")
elif eng == 1:
    print("Script: English")
    if word in set_of_eng_words:
        print("Language: English")
    else:
        try:
            y = eng_to_guj(word)
            print("translate Gujarati word: ", y)
            g = guj_iwn.synsets(y)
            print("Language: Gujarati")
        except:
            print("Language is not Gujarati")
        try:
            x = eng_to_hindi(word)
            print("translate Hindi word: ", x)
            h = hindi_iwn.synsets(x)
            print("Language: Hindi")
        except:
            print("Language is not Hindi.")
            # if():

elif hindi == 1:
    print("Script: Hindi")
    try:
        x = hindi_iwn.synsets(word)
        print("Language: Hindi")
    except:
        x = hindi_to_eng(word)
        print("Translated English word: ", x)
        if x in set_of_eng_words:
            print("Language: English")
        else:
            print("word not identified.")
else:
    print("Please type only in English, Gujarati or Hindi language.")