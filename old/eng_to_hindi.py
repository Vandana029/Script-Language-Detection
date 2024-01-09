def eng_to_hindi(word):
    consonant1 = {'c': 'क', "k": 'क', "ch": 'च', 't': 'त', 'p': 'प',
                  'kh': 'ख', 'chh': 'छ', 'th': 'थ', 'ph': 'फ', 'f': 'फ',
                  'g': 'ग', 'j': 'ज', 'd': 'द', 'b': 'ब',
                  'gh': 'घ', 'jh': 'झ', 'z': 'झ', 'dh': 'ध', 'bh': 'भ',
                  'ṅa': 'ङ', 'ña': 'ञ', 'n': 'न', 'm': 'म',
                  'y': 'य', 'r': 'र', 'l': 'ल', 'v': 'व', 'w': 'व', 'sh': 'श',
                  's': 'स', 'h': 'ह', 'gy': 'ज्ञ', 'x': 'क्ष'}

    consonant2 = {"t": 'ट', 'th': 'ठ', 'd': 'ड', 'dh': 'ढ', 'n': 'ण', 'sh': 'ष'}

    vowel = {'a': 'अ', 'aa': 'आ', 'i': 'इ', 'ee': 'ई', 'u': 'उ', 'oo': 'ऊ', 'ru': 'ृ', 'ri': 'ऋ',
             'e': 'ए', 'ai': 'ऐ', 'au': 'ओ', 'o': 'औ', 'am': 'अं', 'an': 'अं', 'ah': 'अः'}

    symbol = {'a': '', 'aa': 'ा', 'i': 'ि', 'ee': 'ी', 'u': 'ु', 'oo': 'ू', 'ru': 'ृ', 'e': 'े',
              'ai': 'ै', 'o': 'ो', 'au': 'ौ', 'am': 'ं', 'an': 'ं', 'ah': 'ः'}

    translated_word = ""
    #word = list(input("Enter word: "))
    #print(word)
    first_letter = translated_word + word[0]
    second_letter = first_letter + word[1]
    flagtemp1 = 0
    flagtemp2 = 0
    start = 0

    if second_letter in vowel:
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
            continue
        elif temp2 in symbol:
            if (translated_word[-1] in consonant1.values()) or (
                    translated_word[-2] + translated_word[-1] in consonant1.values()):
                translated_word += symbol[temp2]
                #print(translated_word)
                flagtemp2 = 1
            else:
                translated_word += vowel[temp2]
                #print(translated_word)

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
            exit(1)

        # if temp2 in symbol:
        #     if (translated_word[-1] in consonant1.values()) or (
        #             translated_word[-2] + translated_word[-1] in consonant1.values()):
        #         translated_word += symbol[temp2]
        #         #print(translated_word)
        #         flagtemp2 = 1
        #         continue
        #     else:
        #         translated_word += vowel[temp2]
        #         continue
        # if temp1 in symbol:
        #     if (translated_word[-1] in consonant1.values()) or (
        #             translated_word[-2] + translated_word[-1] in consonant1.values()):
        #         translated_word += symbol[temp1]
        #         #print(translated_word)
        #         continue
        #     else:
        #         translated_word += vowel[temp1]
        #         #print(translated_word)

    if flagtemp2 == 0:
        if word[i + 1] in consonant1:
            translated_word += consonant1[word[i + 1]]
        elif (translated_word[-1] in consonant1.values()) or (
                translated_word[-2] + translated_word[-1] in consonant1.values()):
            translated_word += symbol[word[i + 1]]
        else:
            translated_word += vowel[word[i + 1]]

    #print(translated_word)
    return translated_word
