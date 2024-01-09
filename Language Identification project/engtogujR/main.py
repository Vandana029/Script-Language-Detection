
consonant1 = {"k": 'ક', "ch": 'ચ', 't': 'ત', 'p': 'પ',
              'kh': 'ખ', 'chh': 'છ', 'th': 'થ', 'ph': 'ફ', 'f': 'ફ',
              'g': 'ગ', 'j': 'જ', 'd': 'દ', 'b': 'બ',
              'gh': 'ઘ', 'jh': 'ઝ', 'z': 'ઝ', 'dh': 'ધ', 'bh': 'ભ',
              'ṅa': 'ઙ', 'ña': 'ઞ', 'n': 'ન', 'm': 'મ',
              'y': 'ય', 'r': 'ર', 'l': 'લ', 'v': 'વ', 'w': 'વ', 'sh': 'શ',
              's': 'સ', 'h': 'હ', 'gy': 'જ્ઞ', 'x': 'ક્ષ', 'ksh': 'ક્ષ'}
consonant2 = {"t": 'ટ', 'th': 'ઠ', 'd': 'ડ', 'dh': 'ઢ', 'n': 'ણ', 'l': 'ળ', 'sh': 'ષ'}
vowel = {'a': 'અ', 'aa': 'આ', 'i': 'ઇ', 'ee': 'ઈ', 'u': 'ઉ', 'oo': 'ઊ', 'ru': 'ૃ',
         'e': 'એ', 'ai': 'ઐ', 'au': 'ઔ', 'o': 'ઓ', 'am': 'ં', 'an': 'ં'}
symbol = {'a': "", 'aa': 'ા', 'i': 'િ', 'ee': 'ી', 'u': 'ુ', 'oo': 'ૂ', 'ru': 'ૃ', 'e': 'ે', 'ai': 'ૈ',
          'o': 'ો', 'au': 'ૌ', 'am': 'ં', 'an': 'ં', '્': ""}

word = list(input("Enter word: "))
print(word)

translated_word = ""
if len(word) >= 3:
    first_letter = translated_word + word[0]
    second_letter = first_letter + word[1]
    third_letter = second_letter + word[2]
elif len(word) == 2:
    first_letter = translated_word + word[0]
    second_letter = first_letter + word[1]
else:
    if word[0] in consonant1:
        translated_word += consonant1[word]
    elif word[0] in vowel:
        translated_word += consonant1[word]
    else:
        print("Please type in English, Hindi or Gujarati language only.")
        exit(0)

flagtemp1 = 0
flagtemp2 = 0
start = 0

if third_letter in consonant1:
    translated_word += consonant1[third_letter]

    start = 4
elif second_letter in vowel:
    translated_word += vowel[second_letter]
    #print(translated_word)
    start = 2
elif first_letter in vowel:
    translated_word += vowel[first_letter]
    #print(translated_word)
    start = 1

# print(translated_word)
for i in range(start, len(word) - 1):
    if flagtemp2 == 1:
        flagtemp2 = 0
        continue
    temp1 = word[i]
    temp2 = word[i] + word[i + 1]

    if temp2 in consonant1:
        translated_word += consonant1[temp2]
        #print(translated_word)
        flagtemp2 = 1
    elif temp2 in symbol:
        if (translated_word[-1] in consonant1.values()) or (
                translated_word[-2] + translated_word[-1] in consonant1.values()):
            translated_word += symbol[temp2]
            #print(translated_word)
            flagtemp2 = 1
            continue
        else:
            translated_word += vowel[temp2]
            continue
    elif temp1 in consonant1:
        translated_word += consonant1[temp1]
        #print(translated_word)
        continue
    elif temp1 in symbol:
        if (translated_word[-1] in consonant1.values()) or (
                translated_word[-2] + translated_word[-1] in consonant1.values()):
            translated_word += symbol[temp1]
            #print(translated_word)
            continue
        else:
            translated_word += vowel[temp1]
            #print(translated_word)
    else:
        print("Please type in English, Hindi or Gujarati language only.")
        exit(0)

if flagtemp2 == 0:
    if word[i + 1] in consonant1:
        translated_word += consonant1[word[i + 1]]
    elif (translated_word[-1] in consonant1.values()) or (
            translated_word[-2] + translated_word[-1] in consonant1.values()):
        translated_word += symbol[word[i + 1]]
    else:
        translated_word += vowel[word[i + 1]]

print(translated_word)

