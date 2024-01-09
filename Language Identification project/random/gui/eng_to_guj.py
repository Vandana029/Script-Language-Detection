# use list to generate possible inputs from given input words
# ['પંઇ', 'પનિ', 'પંઈ', 'પની'] to
# ['પિ', 'પંઇ', 'પનિ', 'પણિ', 'પાનિ', 'પાણિ', 'પી', 'પંઈ', 'પની', 'પણી', 'પાની', 'પાણી']
# Eg: from 'kaisa' to ['kaisa', 'kaaisa', 'kaisaa']

def eng_to_guj(word):
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
                  'y ': 'ય', 'r': 'ર', 'l': 'ળ', 'v': 'વ', 'w': 'વ', 'sh': 'ષ',
                  's': 'સ', 'h': 'હ', 'gn': 'જ્ઞ', 'x': 'ક્ષ', '1': 'ક્ષ',
                  't1': 'ટ', 'th1': 'થ', 'd1': 'ડ', 'dh1': 'ઢ', 'n1': 'ણ', 'l1': 'લ', 'sh1': 'શ'}
    vowel = {'a': ['અ', 'આ'], 'aa': 'આ', 'i': ['ઇ', 'ઈ'], 'ee': 'ઈ', 'u': 'ઉ', 'oo': 'ઊ', 'ru': 'ઋ',
             'e': 'એ', 'ai': 'ઐ', 'au': 'ઔ', 'o': 'ઓ', 'am': 'અં', 'an': 'અં', 'ah': 'અઃ',
             ' ': ''}
    symbol = {'a': ["", 'ા'], 'aa': 'ા', 'i': ['િ', 'ી'], 'ee': 'ી', 'u': ['ુ', 'ૂ'], 'oo': 'ૂ', 'ru': 'ૃ',
              'e': 'ે', 'ai': 'ૈ', 'o': 'ો', 'au': 'ૌ', 'am': 'ં',
              'an': 'ં', '્': "", ' ': ' '}

    # word = input("Enter: ")
    input_word = word.lower()
    word1 = input_word.replace('ksh', '1')
    # print("Entered word: ", input_word)
    word = list(word1.replace('chh', '0'))
    # print("word", word)
    # print(word)

    translated_word_list = []
    translated_word = ""

    if len(word) == 1:
        if word[0] in consonant1:
            if isinstance(consonant1[word[0]], list):
                for k in consonant1[word[0]]:
                    translated_word_list.append(k)
            else:
                translated_word_list.append(consonant1[word[0]])
        else:
            if isinstance(vowel[word[0]], list):
                for k in vowel[word[0]]:
                    translated_word_list.append(k)
            else:
                translated_word_list.append(vowel[word[0]])
        return translated_word_list
        # print(translated_word_list)
        # exit(0)

    first_letter = translated_word + word[0]
    second_letter = first_letter + word[1]

    if len(word) == 2:
        if second_letter in consonant1:
            if isinstance(consonant1[second_letter], list):
                translated_word_list.append(consonant1[second_letter][0])
                translated_word_list.append(consonant1[second_letter][1])
            else:
                translated_word_list.append(consonant1[second_letter])
        elif second_letter in vowel:
            if isinstance(vowel[second_letter], list):
                for j in vowel[second_letter]:
                    translated_word_list.append(j)
            else:
                translated_word_list.append(vowel[second_letter])
        elif word[0] in vowel and word[1] in vowel:
            if isinstance(vowel[word[0]], list):
                translated_word_list.append(vowel[word[0]][0])
                translated_word_list.append(vowel[word[0]][1])
            else:
                translated_word_list.append(vowel[word[0]])
            if isinstance(vowel[word[1]], list):
                for j in range(len(translated_word_list)):
                    x = translated_word_list[j]
                    translated_word_list[j] += vowel[word[1][0]]
                    translated_word_list.append(x + vowel[word[1][1]])
            else:
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += vowel[word[1]]
        elif word[0] in consonant1 and word[1] in vowel:
            if isinstance(consonant1[word[0]], list):
                translated_word_list.append(consonant1[word[0]][0])
                translated_word_list.append(consonant1[word[0]][1])
            else:
                translated_word_list.append(consonant1[word[0]])
            if isinstance(symbol[word[1]], list):
                for j in range(len(translated_word_list)):
                    x = translated_word_list[j]
                    translated_word_list[j] += symbol[word[1][0]]
                    translated_word_list.append(x + symbol[word[1][1]])
            else:
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += symbol[word[1]]
        elif word[0] in vowel and word[1] in consonant1:
            if isinstance(vowel[word[0]], list):
                translated_word_list.append(vowel[word[0]][0])
                translated_word_list.append(vowel[word[0]][1])
            else:
                translated_word_list.append(vowel[word[0]])
            if isinstance(consonant1[word[1]], list):
                for j in range(len(translated_word_list)):
                    x = translated_word_list[j]
                    translated_word_list[j] += consonant1[word[1][0]]
                    translated_word_list.append(x + consonant1[word[1][1]])
            else:
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += consonant1[word[1]]
        elif word[0] in consonant1 and word[1] in consonant1:
            if isinstance(consonant1[word[0]], list):
                translated_word_list.append(consonant1[word[0]][0])
                translated_word_list.append(consonant1[word[0]][1])
            else:
                translated_word_list.append(consonant1[word[0]])
            if isinstance(consonant1[word[1]], list):
                for j in range(len(translated_word_list)):
                    x = translated_word_list[j]
                    translated_word_list[j] += '્' + consonant1[word[1]][0]
                    translated_word_list.append(x + '્' + consonant1[word[1]][1])
            else:
                # print(translated_word_list)
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += '્' + consonant1[word[1]]
        return translated_word_list
        # print(translated_word_list)
        # exit(0)

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

    # print(translated_word, '*')

    def cons_temp1(letter, lst, a):
        if not lst:
            if isinstance(consonant1[letter], list):
                for p in consonant1[letter]:
                    lst.append(p)
            else:
                lst.append(consonant1[letter])
        else:
            if a != 0:
                if a == 1 and word[0] in consonant1:
                    for y in range(len(lst)):
                        lst[y] += '્'
                elif a >= 2:
                    for p in range(len(lst)):
                        if (word[a - 1] not in symbol or word[a - 2] + word[a - 1] not in symbol) and (
                                lst[p][-1] in consonant2.values() or lst[p][-2] +
                                lst[p][-1] in consonant2.values()) and (
                                word[a - 2] + word[a - 1] in consonant1 or word[a - 1] in consonant1):
                            lst[p] += '્'
                            if lst[p][-2] in ['ન', 'મ']:
                                b = lst[p][:-2] + 'ં'
                                lst.append(b)
            if isinstance(consonant1[letter], list):
                templist = lst.copy()
                for y in range(len(lst)):
                    lst[y] += consonant1[letter][0]
                for y in range(len(templist)):
                    templist[y] += consonant1[letter][1]
                lst = lst + templist
                # for k in consonant1[temp2]:
                #     translated_word_list.append(k)
            else:
                for y in range(len(lst)):
                    lst[y] += consonant1[letter]
        # print(lst)
        return lst

    def sym_temp1(letter, lst, a):
        for p in range(len(lst)):
            if len(word) != 3 and a == 1 and word[0] in vowel:
                if isinstance(vowel[letter], list):
                    b = lst[p]
                    lst[p] += vowel[letter][0]
                    lst.append(b + vowel[letter][1])
                else:
                    lst[p] += vowel[letter]
            elif len(word) != 3 and a == 2 and word[0] + word[1] in vowel:
                if isinstance(vowel[letter], list):
                    b = lst[p]
                    lst[p] += vowel[letter][0]
                    lst.append(b + vowel[letter][1])
                else:
                    lst[p] += vowel[letter]
            elif len(word) != 3 and (lst[p][-1] in consonant2.values() or
                                     lst[p][-2] + lst[p][
                                         -1] in consonant2.values()) and (
                    word[a - 2] + word[a - 1] in consonant1 or word[a - 1] in consonant1):
                if isinstance(symbol[letter], list):
                    b = lst[p]
                    lst[p] += symbol[letter][0]
                    lst.append(b + symbol[letter][1])
                else:
                    lst[p] += symbol[letter]
            elif len(word) == 3 and lst[p][-1] in consonant2.values():
                if isinstance(symbol[letter], list):
                    b = lst[p]
                    lst[p] += symbol[letter][0]
                    lst.append(b + symbol[letter][1])
                else:
                    lst[p] += symbol[letter]
            else:
                if isinstance(vowel[letter], list):
                    b = lst[p]
                    lst[p] += vowel[letter][0]
                    lst.append(b + vowel[letter][1])
                else:
                    lst[p] += vowel[letter]
            # print(lst)
        return lst

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
                # print(translated_word_list, '1')
            else:
                if i != 0:
                    if i == 1 and word[0] in consonant1:
                        for j in range(len(translated_word_list)):
                            translated_word_list[j] += '્'
                        # print(translated_word_list, '2')
                    elif i >= 2:
                        for k in range(len(translated_word_list)):
                            if (translated_word_list[k][-1] in consonant2.values() or translated_word_list[k][-2] +
                                translated_word_list[k][-1] in consonant2.values()) and (
                                    word[i - 2] + word[i - 1] in consonant1 or word[i - 1] in consonant1):
                                translated_word_list[k] += '્'
                                if translated_word_list[k][-2] in ['ન', 'મ']:
                                    x = translated_word_list[k][:-2] + 'ં'
                                    translated_word_list.append(x)
                        #         print(translated_word_list, '3')
                        #     print(translated_word_list, '4')
                        # print(translated_word_list, '5')
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

            # print(translated_word_list, "6")
            flagtemp2 = 1
            continue
        elif temp2 in symbol:
            list2 = translated_word_list.copy()
            if temp1 in consonant1:
                list2 = cons_temp1(temp1, list2, i).copy()
            if temp1 in symbol:
                list2 = sym_temp1(temp1, list2, i).copy()

            if word[i + 1] in consonant1:
                list2 = cons_temp1(word[i + 1], list2, i + 1).copy()
            if word[i + 1] in symbol:
                list2 = sym_temp1(word[i + 1], list2, i + 1).copy()
            for k in range(len(translated_word_list)):
                if len(word) != 3 and i == 1 and word[0] in vowel:
                    if isinstance(vowel[temp2], list):
                        x = translated_word_list[k]
                        translated_word_list[k] += vowel[temp2][0]
                        translated_word_list.append(x + vowel[temp2][1])
                    else:
                        translated_word_list[k] += vowel[temp2]
                elif len(word) != 3 and i == 2 and word[0] + word[1] in vowel:
                    if isinstance(vowel[temp2], list):
                        x = translated_word_list[k]
                        translated_word_list[k] += vowel[temp2][0]
                        translated_word_list.append(x + vowel[temp2][1])
                    else:
                        translated_word_list[k] += vowel[temp2]
                elif len(word) != 3 and (
                        translated_word_list[k][-1] in consonant2.values() or translated_word_list[k][-2] +
                        translated_word_list[k][-1] in consonant2.values()) and (
                        word[i - 2] + word[i - 1] in consonant1 or word[i - 1] in consonant1):
                    if isinstance(symbol[temp2], list):
                        for j in symbol[temp2]:
                            translated_word_list.append(translated_word_list[k] + j)
                            print(translated_word_list[k], j)
                        translated_word_list.pop(k)

                        # x = translated_word_list[k]
                        # translated_word_list[k] += symbol[temp2][0]
                        # translated_word_list.append(x + symbol[temp2][1])
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
            translated_word_list = translated_word_list + list2
            # print(translated_word_list, '7')
            flagtemp2 = 1
            continue
        elif temp1 in consonant1:
            # translated_word += consonant1[temp1]
            # print(translated_word, "8")
            translated_word_list = cons_temp1(temp1, translated_word_list, i).copy()
            # print(translated_word_list, '8')
            continue
        elif temp1 in symbol:
            translated_word_list = sym_temp1(temp1, translated_word_list, i).copy()
            # print(translated_word_list, '9')
    if flagtemp2 == 0:
        if len(word) == 3 and word[2] in vowel:
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
        elif word[i + 1] in consonant1:
            for k in range(len(translated_word_list)):
                if (translated_word_list[k][-1] in consonant2.values() or translated_word_list[k][-2] +
                    translated_word_list[k][-1] in consonant2.values()) and (
                        word[i - 1] + word[i] in consonant1 or word[i] in consonant1):
                    translated_word_list[k] += '્'
                    if translated_word_list[k][-2] in ['ન', 'મ']:
                        x = translated_word_list[k][:-2] + 'ં'
                        translated_word_list.append(x)
            if isinstance(consonant1[word[i + 1]], list):
                templist = translated_word_list.copy()
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += consonant1[word[i + 1]][0]
                    if consonant1[word[i + 1]][0] in ['ન', 'મ'] and (
                            word[i - 1] + word[i] in symbol or word[i] in symbol):
                        translated_word_list.append(translated_word_list[j][:-1] + 'ં')
                for j in range(len(templist)):
                    templist[j] += consonant1[word[i + 1]][1]
                    if consonant1[word[i + 1]][1] in ['ન', 'મ'] and (
                            word[i - 1] + word[i] in symbol or word[i] in symbol):
                        templist.append(templist[j][:-1] + 'ં')
                translated_word_list = translated_word_list + templist
            else:
                for j in range(len(translated_word_list)):
                    translated_word_list[j] += consonant1[word[i + 1]]
                    if consonant1[word[i + 1]] in ['ન', 'મ'] and (word[i - 1] + word[i] in symbol or word[i] in symbol):
                        translated_word_list.append(translated_word_list[j][:-1] + 'ં')
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
    return translated_word_list
    # print(translated_word_list)
    # print(set(translated_word_list))
    # print(len(set(translated_word_list)))
