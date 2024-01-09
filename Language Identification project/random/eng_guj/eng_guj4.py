#
# Eg: ['મ્રો', 'મારો'] to ['મરો', 'મારો']

consonant1 = {'c': 'સી', "k": 'ક', "ch": 'ચ', 't': ['ત', 'ટ'], 'p': 'પ',
              'kh': 'ખ', '0': 'છ', 'th': ['થ', 'ઠ'], 'ph': 'ફ', 'f': 'ફ',
              'g': 'ગ', 'j': 'જ', 'd': ['દ', 'ડ'], 'b': 'બ',
              'gh': 'ઘ', 'jh': 'ઝ', 'z': 'ઝ', 'dh': ['ધ', 'ઢ'], 'bh': 'ભ',
              'ṅa': 'ઙ', 'ña': 'ઞ', 'n': ['ન', 'ણ'], 'm': 'મ', 'q': 'ક',
              'y': 'ય', 'r': 'ર', 'l': ['લ', 'ળ'], 'v': 'વ', 'w': 'વ', 'sh': ['શ', 'ષ'],
              's': 'સ', 'h': 'હ', 'gn': 'જ્ઞ', 'x': 'ક્ષ', '1': 'ક્ષ'}
consonant2 = {'c': 'સી', "k": 'ક', "ch": 'ચ', 't': 'ત', 'p': 'પ',
              'kh': 'ખ', '0': 'છ', 'th': 'ઠ', 'ph': 'ફ', 'f': 'ફ',
              'g': 'ગ', 'j': 'જ', 'd': 'દ', 'b': 'બ',
              'gh': 'ઘ', 'jh': 'ઝ', 'z': 'ઝ', 'dh': 'ધ', 'bh': 'ભ',
              'ṅa': 'ઙ', 'ña': 'ઞ', 'n': 'ન', 'm': 'મ', 'q': 'ક',
              'y': 'ય', 'r': 'ર', 'l': 'ળ', 'v': 'વ', 'w': 'વ', 'sh': 'ષ',
              's': 'સ', 'h': 'હ', 'gn': 'જ્ઞ', 'x': 'ક્ષ', '1': 'ક્ષ',
              't1': 'ટ', 'th1': 'થ', 'd1': 'ડ', 'dh1': 'ઢ', 'n1': 'ણ', 'l1': 'લ', 'sh1': 'શ'}
vowel = {'a': ['અ', 'આ'], 'aa': 'આ', 'i': ['ઇ', 'ઈ'], 'ee': 'ઈ', 'u': 'ઉ', 'oo': 'ઊ', 'ru': ['ઋ', 'રુ'],
         'e': 'એ', 'ai': 'ઐ', 'au': 'ઔ', 'o': 'ઓ', 'am': 'અં', 'an': 'અં', 'ah': ['અઃ', 'હ'],
         ' ': ' '}
symbol = {'a': ["", 'ા'], 'aa': 'ા', 'i': ['િ', 'ી'], 'ee': 'ી', 'u': ['ુ', 'ૂ'], 'oo': 'ૂ', 'ru': 'ૃ', 'e': 'ે',
          'ai': 'ૈ', 'o': 'ો', 'au': 'ૌ', 'am': ['ં', 'મ'], 'an': ['ં', 'ન'], '્': "", ' ': ' '}

word = input("Enter: ")
input_word = word.lower()
word1 = input_word.replace('ksh', '1')
# print("Entered word: ", input_word)
word = list(word1.replace('chh', '0'))
print("word", word)
print(word)

translated_word_list = []
translated_word = ""

# if len(word) == 1:
#     if word[0] in consonant1:
#         translated_word += consonant1[word[0]]
#         translated_word_list.append(translated_word)
#         translated_word = ""
#     if word[0] in consonant2:
#         translated_word += consonant2[word[0]]
#         translated_word_list.append(translated_word)
#     if word[0] in vowel:
#         translated_word += vowel[word[0]]
#         translated_word_list.append(translated_word)
#     return translated_word_list
#     exit(0)

first_letter = translated_word + word[0]
second_letter = first_letter + word[1]

# if len(word) == 2:
#     # both letters are consonants i.e. kh, ph, etc
#     if second_letter in consonant1:
#         translated_word += consonant1[second_letter]
#         translated_word_list.append(translated_word)
#         translated_word = ''
#
#     # both letters are consonants having more than one translation i.e. th, dh, etc
#     if second_letter in consonant2:
#         translated_word += consonant2[second_letter]
#         translated_word_list.append(translated_word)
#         translated_word = ''
#
#     # both letters are vowel i.e oo, aa, ai, au, ee, etc
#     if second_letter in vowel:
#         translated_word += vowel[second_letter]
#         translated_word_list.append(translated_word)
#
#     # if translation of two letter together is found, then return
#     if len(translated_word_list) != 0:
#         return translated_word_list
#         exit(0)
#
#     # first letter is consonant and second one is consonant or symbol
#     if first_letter in consonant1:
#         translated_word += consonant1[first_letter]
#         # second letter is symbol i.e. ki, pe, etc
#         if word[1] in symbol:
#             if word[1] == 'a':
#                 translated_word += 'ા'
#                 translated_word_list.append(translated_word)
#             else:
#                 translated_word += symbol[word[1]]
#                 translated_word_list.append(translated_word)
#         # second letter is consonant i.e. sw, kt, etc
#         else:
#             translated_word += '્' + consonant1[word[1]]
#             translated_word_list.append(translated_word)
#             translated_word = ''
#         # second letter is having two translation
#         if word[1] in consonant2:
#             translated_word += consonant1[word[0]] + consonant2[word[1]]
#             translated_word_list.append(translated_word)
#         translated_word = ''
#
#     # if first letter is having two translation i.e. t, d, etc
#     if first_letter in consonant2:
#         translated_word += consonant2[first_letter]
#         if word[1] in symbol:
#             if word[1] == 'a':
#                 translated_word += 'ા'
#                 translated_word_list.append(translated_word)
#             else:
#                 translated_word += symbol[word[1]]
#                 translated_word_list.append(translated_word)
#         else:
#             translated_word += '્' + consonant1[word[1]]
#             translated_word_list.append(translated_word)
#             translated_word = ''
#         if word[1] in consonant2:
#             translated_word += consonant2[word[0]] + consonant2[word[1]]
#             translated_word_list.append(translated_word)
#         # translated_word = ''
#
#     # if letter which has 1st letter as consonant found
#     if len(translated_word_list) != 0:
#         return translated_word_list
#
#     # if letter has 1st letter as vowel
#     if first_letter in vowel:
#         translated_word += vowel[first_letter]
#         if word[1] in vowel:
#             translated_word += vowel[word[1]]
#             translated_word_list.append(translated_word)
#         elif word[1] in consonant1:
#             translated_word += consonant1[word[1]]
#             translated_word_list.append(translated_word)
#             translated_word = ''
#         if word[1] in consonant2:
#             translated_word += vowel[word[0]] + consonant2[word[1]]
#             translated_word_list.append(translated_word)
#         if len(translated_word_list) != 0:
#             return translated_word_list
#     exit(0)

flagtemp1 = 0
flagtemp2 = 0
start = 0

if second_letter in vowel:
    # translated_word += vowel[second_letter]
    if isinstance(vowel[second_letter], list):
        for k in vowel[second_letter]:
            translated_word_list.append(k)
    else:
        translated_word_list.append(vowel[second_letter])
    # print(translated_word, "1")
    start = 2
elif first_letter in vowel:
    if isinstance(vowel[first_letter], list):
        for k in vowel[first_letter]:
            translated_word_list.append(k)
    else:
        translated_word_list.append(vowel[first_letter])
    # print(translated_word, "2")
    start = 1
i = start - 1
# print(translated_word)

for i in range(start, len(word) - 1):
    if flagtemp2 == 1:
        flagtemp2 = 0
        continue
    temp1 = word[i]
    temp2 = word[i] + word[i + 1]

    if temp2 in consonant1:
        if not translated_word_list:
            # translated_word += consonant1[temp2]
            # print(translated_word, "3")
            if isinstance(consonant1[temp2], list):
                for k in consonant1[temp2]:
                    translated_word_list.append(k)
            else:
                translated_word_list.append(consonant1[temp2])
            # translated_word_list.append(consonant1[temp2])
            # print(translated_word_list, "1")
            # if temp2 in consonant2:
            #     translated_word_list.append(consonant2[temp2])
            # print(translated_word_list, "2")
        else:
            if i != 0:
                if i == 1 and word[0] in consonant1:
                    for j in range(len(translated_word_list)):
                        translated_word_list[j] += '્'
                elif i >= 2:
                    for k in range(len(translated_word_list)):
                        if (translated_word_list[k][-1] in consonant2.values() or translated_word_list[k][-2] +
                            translated_word_list[k][-1] in consonant2.values()) and (
                                word[i - 2] + word[i - 1] in consonant1 or word[i - 1] in consonant1):
                            translated_word_list[k] += '્'
                    # if (word[i - 2] + word[i - 1] in consonant1) or (word[i - 1] in consonant1):
                    #     if word[i - 2] + word[i - 1] in ['an', 'am']:
                    #         templist = translated_word_list.copy()
                    #         for j in range(len(translated_word_list)):
                    #             translated_word_list[j] += '્'
                    #         for j in range(len(templist)):
                    #             templist[j] += ''
                    #         translated_word_list = translated_word_list + templist
                    #     else:
                    #         for j in range(len(translated_word_list)):
                    #             translated_word_list[j] += '્'

            if isinstance(consonant1[temp2], list):
                templist = translated_word_list.copy()
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += consonant1[temp2][0]
                for j in range(len(templist)):
                    templist[j] += consonant1[temp2][1]
                translated_word_list = translated_word_list + templist
                # for k in consonant1[temp2]:
                #     translated_word_list.append(k)
            else:
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += consonant1[temp2]
            # translated_word += consonant1[temp2]
            # print(translated_word, "4")
            # if temp2 in consonant2:
            #     templist = []
            #     templist = translated_word_list.copy()
            #     for j in range(len(translated_word_list)):
            #         translated_word_list[j] += consonant1[temp2]
            #     for j in range(len(templist)):
            #         templist[j] += consonant2[temp2]
            #     translated_word_list = translated_word_list + templist
            #     #print(translated_word_list, "3")
            # else:
            #     for j in range(len(translated_word_list)):
            #         translated_word_list[j] += consonant1[temp2]

        # if i + 2 <= len(word) - 1 and word[i + 2] in consonant1:
        #     translated_word += '્'
        #     #print(translated_word, "5")
        #     for j in range(len(translated_word_list)):
        #         translated_word_list[j] += '્'

        # print(translated_word_list, "4")
        flagtemp2 = 1
        continue
    elif temp2 in symbol:
        for k in range(len(translated_word_list)):
            if len(word) != 3 and (translated_word_list[k][-1] in consonant2.values() or
                                   translated_word_list[k][-2] + translated_word_list[k][-1] in consonant2.values()):
                if isinstance(symbol[temp2], list):
                    x = translated_word_list[k]
                    translated_word_list[k] += symbol[temp2][0]
                    translated_word_list.append(x + symbol[temp2][1])
                else:
                    translated_word_list[k] += symbol[temp2]
            elif len(word) == 3 and translated_word_list[k][-1] in consonant2.values():
                if isinstance(symbol[temp2], list):
                    x = translated_word_list[k]
                    translated_word_list[k] += symbol[temp2][0]
                    translated_word_list.append(x + symbol[temp2][1])
                else:
                    translated_word_list[k] += symbol[temp2]
            else:
                if isinstance(vowel[temp2], list):
                    x = translated_word_list[k]
                    translated_word_list[k] += vowel[temp2][0]
                    translated_word_list.append(x + vowel[temp2][1])
                else:
                    translated_word_list[k] += vowel[temp2]
        flagtemp2 = 1
        # if word[i - 1] in consonant1:
        #     if isinstance(symbol[temp2], list):
        #         templist = translated_word_list.copy()
        #         for j in range(len(translated_word_list)):
        #             translated_word_list[j] += symbol[temp2][0]
        #         for j in range(len(templist)):
        #             templist[j] += symbol[temp2][1]
        #         translated_word_list = translated_word_list + templist
        #     else:
        #         for j in range(len(translated_word_list)):
        #             translated_word_list[j] += symbol[temp2]
        # translated_word += symbol[temp2]
        # print(translated_word, "6")

        # print(translated_word_list, "5")
        # else:
        #     # translated_word += vowel[temp2]
        #     # print(translated_word, "7")
        #     if isinstance(vowel[temp2], list):
        #         templist = translated_word_list.copy()
        #         for j in range(len(translated_word_list)):
        #             translated_word_list[j] += vowel[temp2][0]
        #         for j in range(len(templist)):
        #             templist[j] += vowel[temp2][1]
        #         translated_word_list = translated_word_list + templist
        #     else:
        #         for j in range(len(translated_word_list)):
        #             translated_word_list[j] += vowel[temp2]
        #     flagtemp2 = 1
        # print(translated_word_list, "6")
        continue
    elif temp1 in consonant1:
        # translated_word += consonant1[temp1]
        # print(translated_word, "8")
        if not translated_word_list:
            if isinstance(consonant1[temp1], list):
                for k in consonant1[temp1]:
                    translated_word_list.append(k)
            else:
                translated_word_list.append(consonant1[temp1])
            # translated_word_list.append(consonant1[temp1])
            # #print(translated_word_list, "7")
            # if temp1 in consonant2:
            #     translated_word_list.append(consonant2[temp1])
            #     #print(translated_word_list, "8")
        else:
            if i != 0:
                if i == 1 and word[0] in consonant1:
                    for j in range(len(translated_word_list)):
                        translated_word_list[j] += '્'
                elif i >= 2:
                    for k in range(len(translated_word_list)):
                        if (translated_word_list[k][-1] in consonant2.values() or translated_word_list[k][-2] +
                            translated_word_list[k][-1] in consonant2.values()) and (
                                word[i - 2] + word[i - 1] in consonant1 or word[i - 1] in consonant1):
                            translated_word_list[k] += '્'
                    # if (word[i - 2] + word[i - 1] in consonant1) or word[i - 1] in consonant1:
                    #     if word[i - 2] + word[i - 1] in ['an', 'am']:
                    #         templist = translated_word_list.copy()
                    #         for j in range(len(translated_word_list)):
                    #             translated_word_list[j] += '્'
                    #         for j in range(len(templist)):
                    #             templist[j] += ''
                    #         translated_word_list = translated_word_list + templist
                    #     else:
                    #         for j in range(len(translated_word_list)):
                    #             translated_word_list[j] += '્'
                    #     # for j in range(len(translated_word_list)):
                    #     #     translated_word_list[j] += '્'
            if isinstance(consonant1[temp1], list):
                templist = translated_word_list.copy()
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += consonant1[temp1][0]
                for j in range(len(templist)):
                    templist[j] += consonant1[temp1][1]
                translated_word_list = translated_word_list + templist
                # for k in consonant1[temp2]:
                #     translated_word_list.append(k)
            else:
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += consonant1[temp1]
            # if temp1 in consonant2:
            #     templist = []
            #     templist = translated_word_list.copy()
            #     for j in range(len(translated_word_list)):
            #         translated_word_list[j] += consonant1[temp1]
            #     for j in range(len(templist)):
            #         templist[j] += consonant2[temp1]
            #     translated_word_list = translated_word_list + templist
            #     #print(translated_word_list, "9")
            # else:
            #     for j in range(len(translated_word_list)):
            #         translated_word_list[j] += consonant1[temp1]
        # if i + 1 <= len(word) - 1 and word[i + 1] in consonant1:
        #     if i + 2 <= len(word) - 1 and word[i + 1] + word[i + 2] == 'ru':
        #         continue
        #     translated_word += '્'
        #     # print(translated_word, '9')
        #     for j in range(len(translated_word_list)):
        #         translated_word_list[j] += '્'
        #     # print(translated_word_list, "10")
        continue
    elif temp1 in symbol:
        for k in range(len(translated_word_list)):

            if len(word) != 3 and (translated_word_list[k][-1] in consonant2.values() or
                                   translated_word_list[k][-2] + translated_word_list[k][-1] in consonant2.values()):
                if isinstance(symbol[temp1], list):
                    x = translated_word_list[k]
                    translated_word_list[k] += symbol[temp1][0]
                    translated_word_list.append(x + symbol[temp1][1])
                else:
                    translated_word_list[k] += symbol[temp1]
            elif len(word) == 3 and translated_word_list[k][-1] in consonant2.values():
                if isinstance(symbol[temp1], list):
                    x = translated_word_list[k]
                    translated_word_list[k] += symbol[temp1][0]
                    translated_word_list.append(x + symbol[temp1][1])
                else:
                    translated_word_list[k] += symbol[temp1]
            else:
                if isinstance(vowel[temp1], list):
                    x = translated_word_list[k]
                    translated_word_list[k] += vowel[temp1][0]
                    translated_word_list.append(x + vowel[temp1][1])
                else:
                    translated_word_list[k] += vowel[temp1]
        # if word[i - 1] in consonant1:
        #     if isinstance(symbol[temp1], list):
        #         templist = translated_word_list.copy()
        #         for j in range(len(translated_word_list)):
        #             translated_word_list[j] += symbol[temp1][0]
        #         for j in range(len(templist)):
        #             templist[j] += symbol[temp1][1]
        #         translated_word_list = translated_word_list + templist
        #     else:
        #         for j in range(len(translated_word_list)):
        #             translated_word_list[j] += symbol[temp1]
        # else:
        #     # translated_word += vowel[temp2]
        #     # print(translated_word, "7")
        #     if isinstance(vowel[temp1], list):
        #         templist = translated_word_list.copy()
        #         for j in range(len(translated_word_list)):
        #             translated_word_list[j] += vowel[temp1][0]
        #         for j in range(len(templist)):
        #             templist[j] += vowel[temp1][1]
        #         translated_word_list = translated_word_list + templist
        #     else:
        #         for j in range(len(translated_word_list)):
        #             translated_word_list[j] += vowel[temp1]
#         if word[i - 1] in consonant1:
#             translated_word += symbol[temp1]
#             #print(translated_word, "10")
#             for j in range(len(translated_word_list)):
#                 translated_word_list[j] += symbol[temp1]
#             #print(translated_word_list, "11")
#         else:
#             translated_word += vowel[temp1]
#             #print(translated_word, '11')
#             for j in range(len(translated_word_list)):
#                 translated_word_list[j] += vowel[temp1]
#             #print(translated_word_list, "12")
# #print(word[0] + word[2], '**')
if flagtemp2 == 0:
    if len(word) == 3 and word[0] + word[1] in vowel:
        if word[2] in vowel:
            if isinstance(vowel[word[2]], list):
                templist = translated_word_list.copy()
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += vowel[word[2]][0]
                for j in range(len(templist)):
                    templist[j] += vowel[word[2]][1]
                translated_word_list = translated_word_list + templist
            else:
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += vowel[word[2]]

            # translated_word += vowel[word[2]]
            # translated_word_list.append(translated_word)
            # print(translated_word, "16")
            # print(translated_word_list, "17")
        elif word[2] in consonant1:
            if isinstance(consonant1[word[2]], list):
                templist = translated_word_list.copy()
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += consonant1[word[2]][0]
                for j in range(len(templist)):
                    templist[j] += consonant1[word[2]][1]
                translated_word_list = translated_word_list + templist
            else:
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += consonant1[word[2]]
            # temp = translated_word
            # translated_word += consonant2[word[2]]
            # temp += consonant1[word[2]]
            # translated_word_list.append(translated_word)
            # translated_word_list.append(temp)
            # #print(translated_word, "17")
            # #print(translated_word_list, "18")
        # else:
        #     translated_word += consonant1[word[2]]
        #     translated_word_list.append(translated_word)
        #     #print(translated_word, "18")
        #     #print(translated_word_list, "19")
    # elif len(word) == 3 and word[0] + word[1] in vowel
    elif word[i + 1] in consonant1:
        for k in range(len(translated_word_list)):
            if (translated_word_list[k][-1] in consonant2.values() or translated_word_list[k][-2] +
                translated_word_list[k][-1] in consonant2.values()) and (
                    word[i - 1] + word[i] in consonant1 or word[i] in consonant1):
                translated_word_list[k] += '્'
        # if word[i] in consonant1:
        #     for j in range(len(translated_word_list)):
        #         translated_word_list[j] += '્'
        if isinstance(consonant1[word[i + 1]], list):
            templist = translated_word_list.copy()
            for j in range(len(translated_word_list)):
                translated_word_list[j] += consonant1[word[i + 1]][0]
            for j in range(len(templist)):
                templist[j] += consonant1[word[i + 1]][1]
            translated_word_list = translated_word_list + templist
        else:
            for j in range(len(translated_word_list)):
                translated_word_list[j] += consonant1[word[i + 1]]

        # translated_word += consonant1[word[i + 1]]
        # if word[i + 1] in consonant2:
        #     templist = []
        #     templist = translated_word_list.copy()
        #     for j in range(len(translated_word_list)):
        #         translated_word_list[j] += consonant1[word[i + 1]]
        #     for j in range(len(templist)):
        #         templist[j] += consonant2[word[i + 1]]
        #     translated_word_list = translated_word_list + templist
        #     #print(translated_word_list, "13")
        # else:
        #     for j in range(len(translated_word_list)):
        #         translated_word_list[j] += consonant1[word[i + 1]]
        #     #print(translated_word_list, "14")
        # #print(translated_word, '12')
    elif word[i] in consonant1:
        for k in range(len(translated_word_list)):
            if (translated_word_list[k][-1] in consonant2.values()) or (
                    translated_word_list[k][-2] + translated_word_list[k][-1] in consonant2.values()):
                if isinstance(symbol[word[i + 1]], list):
                    x = translated_word_list[k]
                    translated_word_list[k] += symbol[word[i + 1]][0]
                    translated_word_list.append(x + symbol[word[i + 1]][1])
                else:
                    translated_word_list[k] += symbol[word[i + 1]]
            else:
                if isinstance(vowel[word[i + 1]], list):
                    x = translated_word_list[k]
                    translated_word_list[k] += vowel[word[i + 1]][0]
                    translated_word_list.append(x + vowel[word[i + 1]][1])
                else:
                    translated_word_list[k] += vowel[word[i + 1]]
        # print(word[i], '***')
        # if isinstance(symbol[word[i + 1]], list):
        #     templist = translated_word_list.copy()
        #     for j in range(len(translated_word_list)):
        #         translated_word_list[j] += symbol[word[i + 1]][0]
        #     for j in range(len(templist)):
        #         templist[j] += symbol[word[i + 1]][1]
        #     translated_word_list = translated_word_list + templist
        # else:
        #     for j in range(len(translated_word_list)):
        #         translated_word_list[j] += symbol[word[i + 1]]
        # if word[i + 1] == 'a':
        #     translated_word += 'ા'
        #     #print(translated_word, '13')
        #     for j in range(len(translated_word_list)):
        #         translated_word_list[j] += 'ા'
        #     #print(translated_word_list, "14")
        # else:
        #     translated_word += symbol[word[i + 1]]
        #     #print(translated_word, '14')
        #     for j in range(len(translated_word_list)):
        #         translated_word_list[j] += symbol[word[i + 1]]
        #     #print(translated_word_list, "15")
    # else:
    #     if isinstance(vowel[word[i + 1]], list):
    #         templist = translated_word_list.copy()
    #         for j in range(len(translated_word_list)):
    #             translated_word_list[j] += vowel[word[i + 1]][0]
    #         for j in range(len(templist)):
    #             templist[j] += vowel[word[i + 1]][1]
    #         translated_word_list = translated_word_list + templist
    #     else:
    #         for j in range(len(translated_word_list)):
    #             translated_word_list[j] += vowel[word[i + 1]]
    #
    # translated_word += vowel[word[i + 1]]
    # #print(translated_word, '15')
    # for j in range(len(translated_word_list)):
    #     translated_word_list[j] += vowel[word[i + 1]]
    # #print(translated_word_list, "16")
    # # print(translated_word[-3] + translated_word[-2] + translated_word[-1])
print(translated_word_list)
