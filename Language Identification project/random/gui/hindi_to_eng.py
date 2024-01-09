def hindi_to_eng(word):
    dict1 = {'अ': 'a', 'आ': 'aa', 'इ': 'e', 'ई': 'i', 'उ': 'u', 'ऊ': 'oo', 'ऋ': 'ri',
             'ए': 'a', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au', 'अं': 'an', 'अः': 'ah'}

    dict2 = {'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'n',
             'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'n',
             'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n',
             'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n',
             'प': 'p', 'फ': 'f', 'ब': 'b', 'भ': 'bh', 'म': 'm',
             'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v', 'श': 'sh',
             'ष': 'shh', 'स': 's', 'ह': 'h', 'क्ष': 'ksh', 'त्र': 'tr', 'ज्ञ': 'gn'}

    dict3 = {'ा': 'aa', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo', 'ृ': 'ru',
             'ॅ': 'e', 'े': 'e', 'ै': 'ai', 'ॉ': 'o', 'ो': 'o', 'ौ': 'au', '्': "", ' ': " "}

    # store translation from Hindi to english
    s1 = ""
    translated_word_list = []
    # word = list(input("Enter Hindi word: "))
    # print(word)
    ln = len(word)
    # print(ln)
    # indicate letter is in dict3
    flag1 = 0
    # indicate letter is in dict1 means letter is vowel
    flag2 = 0

    for i in range(0, ln - 1):
        # word[i] in dict3 means symbol hence skip, no need to translate
        if flag1 == 1:
            flag1 = 0
            continue
        elif word[i] == ' ':
            s1 += " "
            continue
        elif word[i] in dict1:
            # letter is vowel hence no need to add 'a'
            flag2 = 1
            s1 += dict1[word[i]]
            # print(s1)
        else:
            s1 += dict2[word[i]]
            # print(s1)

        if word[i + 1] not in dict3:
            # letter is consonant
            if flag2 == 0:
                s1 += "a"
                # print(s1)
            # letter is vowel
            else:
                flag2 = 0
        # letter is symbol
        else:
            s1 += dict3[word[i + 1]]
            # print(s1)
            flag1 = 1

    # translate last letter of word
    if ln > 1 and flag1 == 0:
        # letter is symbol
        if word[-1] in dict3:
            s1 += dict3[word[-1]]
        # letter is consonant
        else:
            s1 += dict2[word[-1]]
    # if word is of one length
    elif ln == 1:
        if word[-1] in dict1:
            s1 += dict1[word[-1]]
        else:
            s1 += dict2[word[-1]]
    translated_word_list.append(s1)
    return translated_word_list
