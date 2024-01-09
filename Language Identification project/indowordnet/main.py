import pyiwn
import nltk
nltk.download('words')
from nltk.corpus import words
setofengwords = set(words.words())
#print(list(map(str, pyiwn.Language)))
iwn = pyiwn.IndoWordNet(lang=pyiwn.Language.GUJARATI)

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

word = (input("Enter value: "))
print(word)
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
    print("Script: Gujarati")
    try:
        x = iwn.synsets(word)
        print("Language: Gujarati")
    except:
        print("Language: English")
elif eng == 1:
    print("Script: English")
    if word in setofengwords:
        print("Language: English")
    else:
        print("Language: Gujarati")
else:
    print("Please type only in English or Gujarati language.")

# try:
#   x = iwn.synsets('kite')
#   print("word found")
# except:
#   print("word not found")
